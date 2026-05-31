## Summary

<!-- 変更の概要と背景。関連 issue があれば記載 (Closes #...) -->

## 実行したテスト範囲 / Test scope

<!-- 実行したものにチェックし、ローカルで流したコマンド・結果を残す。必須 -->

- [ ] `just fmt-check` — rustfmt + clippy (`-D warnings`)
- [ ] `just test-unit` — unit tests (no LLVM required)
- [ ] `just test-integration` — e2e tests (requires LLVM 11 + built plugin)
- [ ] `just build` — Clang plugin + Rust reporter
- [ ] Other / manual verification:

## Notes

<!-- レビュアーへの補足、トレードオフ、フォローアップ予定など -->
