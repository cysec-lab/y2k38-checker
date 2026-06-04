# Git Workflow

## Commit Format

Follow conventional commits:

```
<type>(<scope>): <description>

Types: feat | fix | refactor | docs | test | chore | perf | ci
Scope (optional): plugin | reporter | script | ci | docs
```

Examples:
```
feat(plugin): add timet-to-short-downcast check
fix(reporter): handle empty clang output without panic
test(reporter): add unit tests for parse_clang_output edge cases
ci: cache LLVM 11 download in GitHub Actions
```

## Branch Protection

NEVER push directly to `main`. All changes go through a pull request, no matter how small.

## Worktree Usage

When working on multiple features in parallel, use `git worktree` instead of `git stash` or
`git checkout`:

```bash
git fetch origin main
git worktree add ../y2k38-checker-feat-name -b feat/name origin/main
git worktree lock ../y2k38-checker-feat-name  # immediately lock it
```

### Worktree Lifecycle: Lock and Cleanup

Before removing any worktree, verify ALL of the following:

1. `git worktree list` — confirm it is **not** locked
2. `git branch --merged main` — confirm the branch **is** merged
3. `git -C <worktree-path> status` — confirm no uncommitted changes

Only then:
```bash
git worktree remove <path>
git branch -d <branch-name>
```

**NEVER use `--force`** or remove a locked worktree.

## PR Workflow

1. Create feature branch from main: `git checkout -b feat/description origin/main`
2. Make changes, run `just fmt-check && just test-unit` before committing
3. Review full diff: `git diff origin/main...HEAD`
4. Push: `git push -u origin feat/description`
5. Open PR — title follows commit format, body includes test plan

## Implementation Order

1. Use the `planner` agent to design the approach
2. Write tests first (they should fail initially)
3. Implement to make tests pass
4. Use the `code-reviewer` agent before pushing
5. Run `just fmt-check` and `just test-unit` locally before opening PR
