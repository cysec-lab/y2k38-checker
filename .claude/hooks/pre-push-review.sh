#!/usr/bin/env bash
# Pre-push self-review: flags common issues before pushing to remote.
# Called by Claude Code hooks on git push operations.
#
# Note: `set -e` is intentionally NOT used. Most checks below rely on `grep`,
# which exits non-zero when it finds no matches — a normal, expected outcome
# here. We handle failures explicitly instead.
set -uo pipefail

INPUT=$(cat)

# Extract the command being run. If parsing fails, fall back to empty so the
# hook degrades to a no-op rather than blocking the push spuriously.
COMMAND=$(printf '%s' "$INPUT" | python3 -c 'import sys, json
try:
    print(json.load(sys.stdin).get("command", ""))
except Exception:
    pass' 2>/dev/null) || COMMAND=""

# Only run on push operations.
case "$COMMAND" in
    *"git push"*) ;;
    *) exit 0 ;;
esac

# Diff of added lines vs the merge-base (fall back to last commit on a fresh repo).
base=$(git merge-base HEAD origin/main 2>/dev/null) || base="HEAD~1"
DIFF=$(git diff "$base" HEAD -- '*.rs' '*.cpp' '*.h' '*.py' 2>/dev/null) || DIFF=""
ADDED=$(printf '%s\n' "$DIFF" | grep '^+' | grep -v '^+++') || ADDED=""

ISSUES=""

# Unresolved TODO/FIXME/HACK/XXX in new code (excluding known tech-debt markers).
TODOS=$(printf '%s\n' "$ADDED" | grep -E '(TODO|FIXME|HACK|XXX)' \
    | grep -v 'TODO: use env var' | grep -v 'TODO: typed error') || TODOS=""
if [ -n "$TODOS" ]; then
    ISSUES="${ISSUES}\n⚠ Unresolved TODO/FIXME in new code:\n${TODOS}"
fi

# .unwrap() in new non-test Rust code.
UNWRAPS=$(printf '%s\n' "$ADDED" | grep -E '\.unwrap\(\)' \
    | grep -v '#\[cfg(test)\]' | grep -v '// OK:') || UNWRAPS=""
if [ -n "$UNWRAPS" ]; then
    ISSUES="${ISSUES}\n⚠ .unwrap() in new Rust code (use ? or handle the error):\n${UNWRAPS}"
fi

# Hardcoded absolute paths in new code (other than the known CLANG/PLUGIN consts).
HARDCODED=$(printf '%s\n' "$ADDED" | grep -E '"/root/|"/home/' \
    | grep -v 'CLANG_PATH\|PLUGIN_PATH\|const ') || HARDCODED=""
if [ -n "$HARDCODED" ]; then
    ISSUES="${ISSUES}\n⚠ Hardcoded absolute paths in new code:\n${HARDCODED}"
fi

if [ -n "$ISSUES" ]; then
    echo "Pre-push review found potential issues:"
    echo -e "$ISSUES"
    echo ""
    echo "Review the above before pushing. To bypass (not recommended): git push --no-verify"
fi

exit 0
