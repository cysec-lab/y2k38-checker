#!/usr/bin/env bash
# Pre-push self-review: flags common issues before pushing to remote.
# Called by Claude Code hooks on git push operations.

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('command',''))" 2>/dev/null || echo "")

# Only run on push operations
if ! echo "$COMMAND" | grep -q "git push"; then
    exit 0
fi

ISSUES=""

DIFF=$(git diff "$(git merge-base HEAD origin/main 2>/dev/null || echo HEAD~1)" HEAD -- '*.rs' '*.cpp' '*.h' '*.py' 2>/dev/null || git diff HEAD~1 HEAD -- '*.rs' '*.cpp' '*.h' '*.py' 2>/dev/null || true)
ADDED=$(echo "$DIFF" | grep '^+' | grep -v '^+++')

# Check for TODO/FIXME/HACK/XXX in new code (excluding known tech debt comments)
TODOS=$(echo "$ADDED" | grep -E '^\+.*(TODO|FIXME|HACK|XXX)' | grep -v 'TODO: use env var' | grep -v 'TODO: typed error' || true)
if [ -n "$TODOS" ]; then
    ISSUES="${ISSUES}\n⚠ Unresolved TODO/FIXME in new code:\n${TODOS}"
fi

# Check for .unwrap() outside test code in Rust
UNWRAPS=$(echo "$ADDED" | grep -E '^\+.*\.unwrap\(\)' | grep -v '#\[cfg(test)\]' | grep -v '// OK:' || true)
if [ -n "$UNWRAPS" ]; then
    ISSUES="${ISSUES}\n⚠ .unwrap() in new Rust code (use ? or handle the error):\n${UNWRAPS}"
fi

# Check for hardcoded absolute paths (other than the known CLANG_PATH/PLUGIN_PATH constants)
HARDCODED=$(echo "$ADDED" | grep -E '^\+.*"/root/|^\+.*"/home/' | grep -v 'CLANG_PATH\|PLUGIN_PATH\|const ' || true)
if [ -n "$HARDCODED" ]; then
    ISSUES="${ISSUES}\n⚠ Hardcoded absolute paths in new code:\n${HARDCODED}"
fi

if [ -n "$ISSUES" ]; then
    echo "Pre-push review found potential issues:"
    echo -e "$ISSUES"
    echo ""
    echo "Review the above before pushing. To bypass (not recommended): git push --no-verify"
    # Output JSON for Claude Code hook system
    python3 -c "
import json, sys
msg = sys.stdin.read() if False else '''Pre-push review flagged issues — review before pushing.'''
print(json.dumps({'decision': 'block', 'reason': msg}))
" 2>/dev/null || true
fi

exit 0
