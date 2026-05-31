# y2k38-checker

[![CI](https://github.com/cysec-lab/y2k38-checker/actions/workflows/ci.yml/badge.svg)](https://github.com/cysec-lab/y2k38-checker/actions/workflows/ci.yml)
![Platform](https://img.shields.io/badge/platform-Linux%20x86__64-lightgrey)
![License](https://img.shields.io/github/license/cysec-lab/y2k38-checker)

Clang static analyzer plugin that detects [Year 2038 (Y2K38)](https://en.wikipedia.org/wiki/Year_2038_problem) vulnerabilities in C source code.

> **Reference:** [IPSJ Paper](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=228078&item_no=1&page_id=13&block_id=8)

---

## Quick Start

```sh
git clone https://github.com/cysec-lab/y2k38-checker.git
cd y2k38-checker
devbox shell          # installs Nix + toolchain on first run
devbox run setup      # downloads LLVM 11 and builds everything (~700 MB, one-time)
just check file.c
```

**Example output:**

```
dataset/blacklist/read-fs-timestamp.c
- category: ReadFsTimestamp
- row: 9
- column: 24

dataset/blacklist/read-fs-timestamp.c
- category: ReadFsTimestamp
- row: 10
- column: 24
```

---

## What it detects

| Check ID | Trigger | Risk |
|---|---|---|
| `read-fs-timestamp` | Reading `st_atime` / `st_mtime` / `st_ctime` from `struct stat` | ext2/3, XFS (<Linux 5.10), ReiserFS store timestamps as 32-bit integers |
| `write-fs-timestamp` | Calling `utime` / `utimes` / `utimensat` / `futimes` / `futimens` | Same filesystem constraint; writes may silently overflow |
| `timet-to-int-downcast` | Casting `time_t` → `int` | `int` is 32-bit on most platforms; overflows after 2038-01-19 |
| `timet-to-long-downcast` | Casting `time_t` → `long` | `long` is 32-bit on 32-bit platforms and Windows |

---

## Usage

### via the reporter (recommended)

Runs the Clang plugin and formats the results:

```sh
just check path/to/file.c
```

### via the Clang plugin directly

```sh
clang -w -fplugin=checker/build/lib/liby2k38-plugin.so -c path/to/file.c
```

---

## Development

### Requirements

- **OS:** Linux x86_64
- **[devbox](https://www.jetify.com/devbox)** — provides cmake, gcc, Rust toolchain, just, and more via Nix. `devbox.lock` pins exact versions for reproducibility.
- **LLVM 11** — downloaded automatically by `just setup-llvm` (pre-built for `ubuntu-20.04`).

### Build & Test

```sh
devbox shell          # enter the dev environment
just setup-dev        # first time: download LLVM 11 + build plugin + reporter
just test-unit        # fast unit tests — no LLVM required
just test             # full suite including integration tests
just ci-fast          # what CI runs locally: fmt-check + test-unit
just --list           # all available recipes
```

No devbox? Install `cmake`, a C++ compiler, `just`, and a Rust toolchain manually — the `just` recipes work either way.

### Architecture

```
C source file
  │  (subprocess)
  ▼
clang -fplugin=liby2k38-plugin.so   ← Clang plugin (C++, checker/clang-analyzer/)
  │  stderr: "file:row:col: warning: y2k38 (<category>)"
  ▼
Rust reporter (checker/reporter/)   ← parses warnings, formats output
  │
  ▼
Vec<{ category, file, row, column }>
```

See [`docs/spec.md`](docs/spec.md) for the full specification, data flow, and testing strategy.
