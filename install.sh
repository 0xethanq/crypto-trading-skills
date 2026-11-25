#!/bin/sh
# TradeSkill installer.
#   curl -fsSL <origin>/install.sh | sh -s <skill-id|platform|all> [origin]
#   curl -fsSL <origin>/install.sh | sh -s -- --client cursor okx-cex-trade
set -eu

DEFAULT_ORIGIN="https://astraquant.tech"
ORIGIN="${SKILLHUB_ORIGIN:-$DEFAULT_ORIGIN}"
CLIENT=""
DIR="${SKILLS_DIR:-}"
LIST_ONLY=0
TARGETS=""

usage() {
  cat <<'EOF'
Usage:
  curl -fsSL <origin>/install.sh | sh -s <skill-id|platform|all> [options]

Options:
  -c, --client <name>   claude | codex | agents | cursor | opencode | windsurf
  -d, --dir <path>      Target skills directory (overrides SKILLS_DIR and --client)
  -o, --origin <url>    Hub origin URL
  -l, --list            List available platforms and skills
  -h, --help            Show this help
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    -l|--list|list)
      LIST_ONLY=1
      shift
      ;;
    -c|--client)
      [ "$#" -ge 2 ] || { printf 'Missing value for %s\n' "$1" >&2; exit 2; }
      CLIENT="$2"
      shift 2
      ;;
    --client=*)
      CLIENT="${1#*=}"
      shift
      ;;
    -d|--dir)
      [ "$#" -ge 2 ] || { printf 'Missing value for %s\n' "$1" >&2; exit 2; }
      DIR="$2"
      shift 2
      ;;
    --dir=*)
      DIR="${1#*=}"
      shift
      ;;
    -o|--origin)
      [ "$#" -ge 2 ] || { printf 'Missing value for %s\n' "$1" >&2; exit 2; }
      ORIGIN="$2"
      shift 2
      ;;
    --origin=*)
      ORIGIN="${1#*=}"
      shift
      ;;
    http://*|https://*)
      ORIGIN="$1"
      shift
      ;;
    --)
      shift
      while [ "$#" -gt 0 ]; do
        TARGETS="${TARGETS}${TARGETS:+ }$1"
        shift
      done
      ;;
    -*)
      printf 'Unknown option: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
    *)
      TARGETS="${TARGETS}${TARGETS:+ }$1"
      shift
      ;;
  esac
done

if [ -z "$ORIGIN" ]; then
  ORIGIN="$(printf '%s' "${0:-}" | sed -n 's|^\(https\?://[^/]*\).*|\1|p')"
fi
[ -n "$ORIGIN" ] || { printf 'Missing origin. Pass --origin https://example.com or as an argument.\n' >&2; exit 2; }
ORIGIN="${ORIGIN%/}"

if [ "$LIST_ONLY" -eq 0 ] && [ -z "$TARGETS" ]; then
  usage >&2
  exit 2
fi

command -v curl >/dev/null 2>&1 || { printf 'curl is required.\n' >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { printf 'python3 is required.\n' >&2; exit 1; }

client_dir() {
  case "$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')" in
    claude|claude-code) printf '%s/.claude/skills' "$HOME" ;;
    codex|agents) printf '%s/.agents/skills' "$HOME" ;;
    cursor) printf '%s/.cursor/skills' "$HOME" ;;
    opencode) printf '%s/.config/opencode/skills' "$HOME" ;;
    windsurf) printf '%s/.codeium/windsurf/skills' "$HOME" ;;
    *)
      printf 'Unknown client: %s (expected: claude, codex, cursor, opencode, windsurf)\n' "$1" >&2
      exit 2
      ;;
  esac
}

if [ -n "$DIR" ]; then
  DEST="$DIR"
elif [ -n "$CLIENT" ]; then
  DEST="$(client_dir "$CLIENT")"
elif [ -d "$HOME/.claude/skills" ]; then
  DEST="$HOME/.claude/skills"
elif [ -d "$HOME/.agents/skills" ]; then
  DEST="$HOME/.agents/skills"
elif [ -d "$HOME/.cursor/skills" ]; then
  DEST="$HOME/.cursor/skills"
elif [ -d "$HOME/.config/opencode/skills" ]; then
  DEST="$HOME/.config/opencode/skills"
elif [ -d "$HOME/.codeium/windsurf/skills" ]; then
  DEST="$HOME/.codeium/windsurf/skills"
else
  DEST="$HOME/.claude/skills"
fi

TMP="$(mktemp -d 2>/dev/null || mktemp -d -t skillhub)"
trap 'rm -rf "$TMP"' EXIT INT TERM
curl -fsSL "$ORIGIN/catalog.json" -o "$TMP/catalog.json" || { printf 'Cannot read %s/catalog.json\n' "$ORIGIN" >&2; exit 1; }

if [ "$LIST_ONLY" -eq 1 ]; then
  python3 - "$TMP/catalog.json" <<'PY'
import json, sys
cat = json.load(open(sys.argv[1], encoding='utf-8'))
print('Platforms:')
for p in cat.get('platforms', []):
    print(f"  {p['id']:10s} {p.get('brand', p['name'])}")
print('\nPackaged skills:')
for s in cat.get('skills', []):
    if s.get('zip'):
        print(f"  {s['id']:24s} [{s['platform']}] {s.get('title', '')}")
print('\nOfficial-only skills (no hub ZIP):')
for s in cat.get('skills', []):
    if not s.get('zip'):
        print(f"  {s['id']:24s} [{s['platform']}] {s.get('source', '')}")
PY
  exit 0
fi

mkdir -p "$DEST"

PLAN="$TMP/plan.tsv"
python3 - "$TMP/catalog.json" "$PLAN" $TARGETS <<'PY'
import json, sys

cat_path, out_path, *targets = sys.argv[1:]
cat = json.load(open(cat_path, encoding='utf-8'))
skills = cat.get('skills', [])
platforms = {p['id']: p for p in cat.get('platforms', [])}
by_id = {s['id']: s for s in skills}
seen = set()
selected = []

def add_skill(s):
    if s['id'] not in seen:
        seen.add(s['id'])
        selected.append(s)

for t in targets:
    if t == 'all':
        for s in skills:
            if s.get('zip'):
                add_skill(s)
        for p in platforms.values():
            if not any(s.get('zip') for s in skills if s['platform'] == p['id']):
                print(f"Note: {p['id']} skills are provided via official instructions only: {p.get('official', '')}", file=sys.stderr)
    elif t in platforms:
        group = [s for s in skills if s['platform'] == t]
        packaged = [s for s in group if s.get('zip')]
        if not packaged:
            print(f"{t} is provided by the exchange, not as a hub package.", file=sys.stderr)
            print(f"Install it from the official instructions: {platforms[t].get('official', '')}", file=sys.stderr)
            if len(targets) == 1:
                sys.exit(1)
        for s in packaged:
            add_skill(s)
    elif t in by_id:
        s = by_id[t]
        if not s.get('zip'):
            print(f"{t} is provided by the exchange, not as a hub package.", file=sys.stderr)
            print(f"Install it from the official instructions: {s.get('source', '')}", file=sys.stderr)
            if len(targets) == 1:
                sys.exit(1)
        else:
            add_skill(s)
    else:
        print(f"Unknown skill or platform: {t}", file=sys.stderr)
        print(f"Run with --list to see available IDs.", file=sys.stderr)
        sys.exit(1)

if not selected:
    sys.exit(1)

with open(out_path, 'w', encoding='utf-8') as f:
    for s in selected:
        f.write(f"{s['id']}\t{s.get('installDir', '')}\t{s.get('zip', '')}\t{s.get('sha256', '')}\n")
PY

COUNT=0
while IFS="$(printf '\t')" read -r ID META_ID ZIP SHA; do
  [ -n "$ID" ] || continue
  curl -fsSL "$ORIGIN/$ZIP" -o "$TMP/pkg.zip" || { printf 'Download failed: %s\n' "$ORIGIN/$ZIP" >&2; exit 1; }

  if command -v sha256sum >/dev/null 2>&1; then GOT="$(sha256sum "$TMP/pkg.zip" | cut -d' ' -f1)"
  elif command -v shasum >/dev/null 2>&1; then GOT="$(shasum -a 256 "$TMP/pkg.zip" | cut -d' ' -f1)"
  elif command -v openssl >/dev/null 2>&1; then GOT="$(openssl dgst -sha256 "$TMP/pkg.zip" | sed 's/.*= //')"
  else GOT=""; fi

  if [ -n "$GOT" ] && [ -n "$SHA" ] && [ "$GOT" != "$SHA" ]; then
    printf 'Checksum mismatch for %s. Refusing to install.\n' "$ID" >&2
    exit 1
  fi

  rm -rf "$TMP/unpack"
  mkdir -p "$TMP/unpack"
  if command -v unzip >/dev/null 2>&1; then unzip -q "$TMP/pkg.zip" -d "$TMP/unpack"
  else python3 -c 'import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])' "$TMP/pkg.zip" "$TMP/unpack"
  fi

  [ -d "$TMP/unpack/$META_ID" ] || { printf 'Unexpected archive layout for %s.\n' "$ID" >&2; exit 1; }
  rm -rf "$DEST/$META_ID"
  cp -R "$TMP/unpack/$META_ID" "$DEST/$META_ID"
  printf 'Installed %s -> %s\n' "$META_ID" "$DEST/$META_ID"
  COUNT=$((COUNT + 1))
done < "$PLAN"

printf 'Done: %s skill(s) installed in %s\n' "$COUNT" "$DEST"
printf 'Next: read SKILL.md inside each installed folder, then configure the tool it requires.\n'
