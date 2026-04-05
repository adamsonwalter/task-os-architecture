#!/usr/bin/env bash
# Create a new client "company instance" workspace: folder tree + _starters + git init.
# Usage:
#   ./scripts/scaffold_client_workspace.sh /path/to/new-repo-dir "Client Legal Name"
#
# Example:
#   ./scripts/scaffold_client_workspace.sh ~/GitHub/acme-consulting-workspace "Acme Consulting Pty Ltd"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
META_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
DEST="${1:?Usage: $0 /path/to/new-repo-dir \"Client Legal Name\"}"
CLIENT_NAME="${2:?Usage: $0 /path/to/new-repo-dir \"Client Legal Name\"}"
DATE="$(date +%Y-%m-%d)"

if [[ -e "$DEST" ]]; then
  echo "Error: destination already exists: $DEST" >&2
  exit 1
fi

mkdir -p "$DEST"

cp -R "${META_ROOT}/templates/client-workspace/." "$DEST/"
cp -R "${META_ROOT}/_starters" "${DEST}/_starters"

export DEST CLIENT_NAME DATE
python3 <<'PY'
import os
from pathlib import Path

dest = Path(os.environ["DEST"])
client = os.environ["CLIENT_NAME"]
date = os.environ["DATE"]

for path in dest.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix != ".md" and path.name != ".gitignore":
        continue
    text = path.read_text(encoding="utf-8")
    text = text.replace("{CLIENT_ENTITY}", client).replace("{DATE}", date)
    path.write_text(text, encoding="utf-8")
PY

(
  cd "$DEST"
  git init
  git add -A
  if git config user.email >/dev/null 2>&1 && git config user.name >/dev/null 2>&1; then
    git commit -m "Scaffold client AI workspace (${CLIENT_NAME})"
  else
    echo "Note: git user.name / user.email not set — skipped initial commit. Run git commit when configured."
  fi
)

echo "Created: $DEST"
echo "Next: edit company/identity.md and company/strategy.md, then add workflows from _starters/."
