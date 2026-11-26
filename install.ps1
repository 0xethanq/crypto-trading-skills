# TradeSkill PowerShell installer.
#   powershell -NoProfile -Command "& ([scriptblock]::Create((irm <origin>/install.ps1))) <skill-id|platform|all> -Origin <origin>"
[CmdletBinding()]
param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$Target,
    [string]$Client = "",
    [string]$Dir = "",
    [string]$Origin = "",
    [switch]$List,
    [switch]$Help
)

$ErrorActionPreference = "Stop"
$DefaultOrigin = "https://tradeskill.si"

function Show-Usage {
    Write-Host @"
Usage:
  & ([scriptblock]::Create((irm <origin>/install.ps1))) <skill-id|platform|all> [options]

Options:
  -Client <name>   claude | codex | agents | cursor | opencode | windsurf
  -Dir <path>      Target skills directory (overrides SKILLS_DIR and -Client)
  -Origin <url>    Hub origin URL
  -List            List available platforms and skills
  -Help            Show this help
"@
}

if ($Help) {
    Show-Usage
    exit 0
}

$CleanTargets = @()
if ($Target) {
    foreach ($t in $Target) {
        if ($t -match '^https?://') {
            if (-not $Origin) { $Origin = $t }
        } elseif ($t -eq 'list') {
            $List = $true
        } else {
            $CleanTargets += $t
        }
    }
}

if (-not $Origin) {
    if ($env:SKILLHUB_ORIGIN) { $Origin = $env:SKILLHUB_ORIGIN }
    elseif ($DefaultOrigin) { $Origin = $DefaultOrigin }
}
if (-not $Origin) {
    Write-Error "Missing origin. Pass -Origin https://example.com"
    exit 2
}
$Origin = $Origin.TrimEnd('/')

if (-not $List -and $CleanTargets.Count -eq 0) {
    Show-Usage
    exit 2
}

function Resolve-ClientDir([string]$Name) {
    switch ($Name.ToLowerInvariant()) {
        { $_ -in 'claude', 'claude-code' } { return (Join-Path $HOME '.claude\skills') }
        { $_ -in 'codex', 'agents' } { return (Join-Path $HOME '.agents\skills') }
        'cursor' { return (Join-Path $HOME '.cursor\skills') }
        'opencode' { return (Join-Path $HOME '.config\opencode\skills') }
        'windsurf' { return (Join-Path $HOME '.codeium\windsurf\skills') }
        default { throw "Unknown client: $Name (expected: claude, codex, cursor, opencode, windsurf)" }
    }
}

if ($Dir) {
    $Dest = $Dir
} elseif ($env:SKILLS_DIR) {
    $Dest = $env:SKILLS_DIR
} elseif ($Client) {
    $Dest = Resolve-ClientDir $Client
} else {
    $Candidates = @(
        (Join-Path $HOME '.claude\skills'),
        (Join-Path $HOME '.agents\skills'),
        (Join-Path $HOME '.cursor\skills'),
        (Join-Path $HOME '.config\opencode\skills'),
        (Join-Path $HOME '.codeium\windsurf\skills')
    )
    $Dest = $Candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
    if (-not $Dest) { $Dest = $Candidates[0] }
}

$Catalog = Invoke-RestMethod -Uri "$Origin/catalog.json" -UseBasicParsing

if ($List) {
    Write-Host "Platforms:"
    foreach ($p in $Catalog.platforms) {
        $label = if ($p.brand) { $p.brand } else { $p.name }
        Write-Host ("  {0,-10} {1}" -f $p.id, $label)
    }
    Write-Host "`nPackaged skills:"
    foreach ($s in $Catalog.skills) {
        if ($s.zip) {
            Write-Host ("  {0,-24} [{1}] {2}" -f $s.id, $s.platform, $s.title)
        }
    }
    Write-Host "`nOfficial-only skills (no hub ZIP):"
    foreach ($s in $Catalog.skills) {
        if (-not $s.zip) {
            Write-Host ("  {0,-24} [{1}] {2}" -f $s.id, $s.platform, $s.source)
        }
    }
    exit 0
}

$PlatformMap = @{}
foreach ($p in $Catalog.platforms) { $PlatformMap[$p.id] = $p }
$SkillMap = @{}
foreach ($s in $Catalog.skills) { $SkillMap[$s.id] = $s }

$Selected = New-Object System.Collections.Generic.List[object]
$Seen = @{}

function Add-Skill($s) {
    if (-not $Seen.ContainsKey($s.id)) {
        $Seen[$s.id] = $true
        $Selected.Add($s)
    }
}

foreach ($t in $CleanTargets) {
    if ($t -eq 'all') {
        foreach ($s in $Catalog.skills) {
            if ($s.zip) { Add-Skill $s }
        }
        foreach ($p in $Catalog.platforms) {
            $hasZip = $Catalog.skills | Where-Object { $_.platform -eq $p.id -and $_.zip } | Select-Object -First 1
            if (-not $hasZip) {
                Write-Warning "$($p.id) skills are provided via official instructions only: $($p.official)"
            }
        }
    } elseif ($PlatformMap.ContainsKey($t)) {
        $packaged = @($Catalog.skills | Where-Object { $_.platform -eq $t -and $_.zip })
        if ($packaged.Count -eq 0) {
            Write-Warning "$t is provided by the exchange, not as a hub package."
            Write-Warning "Install it from the official instructions: $($PlatformMap[$t].official)"
            if ($CleanTargets.Count -eq 1) { exit 1 }
        }
        foreach ($s in $packaged) { Add-Skill $s }
    } elseif ($SkillMap.ContainsKey($t)) {
        $s = $SkillMap[$t]
        if (-not $s.zip) {
            Write-Warning "$t is provided by the exchange, not as a hub package."
            Write-Warning "Install it from the official instructions: $($s.source)"
            if ($CleanTargets.Count -eq 1) { exit 1 }
        } else {
            Add-Skill $s
        }
    } else {
        Write-Error "Unknown skill or platform: $t (run with -List to see available IDs)"
        exit 1
    }
}

if ($Selected.Count -eq 0) { exit 1 }

New-Item -ItemType Directory -Force -Path $Dest | Out-Null
$Tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("skillhub-" + [System.Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force -Path $Tmp | Out-Null

try {
    $Count = 0
    foreach ($s in $Selected) {
        $ZipPath = Join-Path $Tmp "pkg.zip"
        $UnpackDir = Join-Path $Tmp "unpack"
        if (Test-Path $UnpackDir) { Remove-Item -Recurse -Force $UnpackDir }

        Invoke-WebRequest -Uri "$Origin/$($s.zip)" -OutFile $ZipPath -UseBasicParsing
        if ($s.sha256) {
            $Got = (Get-FileHash -Path $ZipPath -Algorithm SHA256).Hash.ToLowerInvariant()
            if ($Got -ne $s.sha256.ToLowerInvariant()) {
                throw "Checksum mismatch for $($s.id). Refusing to install."
            }
        }

        Expand-Archive -Path $ZipPath -DestinationPath $UnpackDir -Force
        $SrcDir = Join-Path $UnpackDir $s.installDir
        if (-not (Test-Path $SrcDir)) {
            throw "Unexpected archive layout for $($s.id)."
        }
        $TargetDir = Join-Path $Dest $s.installDir
        if (Test-Path $TargetDir) { Remove-Item -Recurse -Force $TargetDir }
        Copy-Item -Recurse -Force -Path $SrcDir -Destination $TargetDir
        Write-Host "Installed $($s.installDir) -> $TargetDir"
        $Count++
    }
    Write-Host "Done: $Count skill(s) installed in $Dest"
    Write-Host "Next: read SKILL.md inside each installed folder, then configure the tool it requires."
} finally {
    if (Test-Path $Tmp) { Remove-Item -Recurse -Force $Tmp }
}
