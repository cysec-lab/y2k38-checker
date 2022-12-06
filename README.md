# fs-y2k38-checker

`fs-y2k38-checker` is [Clang Static Analyzer](https://clang-analyzer.llvm.org/) plugin which detects the [Y2K38](https://en.wikipedia.org/wiki/Year_2038_problem) bug caused by file-system with a 32 bit timestamp.

## Build with CMake

Clone the demo repository.

```sh
git clone https://github.com/cysec-lab/fs-y2k38-checker.git
```

Create a new directory for building.

```sh
mkdir build
```

Change into the new directory.

```sh
cd build
```

Run CMake with the path to the LLVM source.

```sh
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True \
    -DLLVM_DIR=</path/to/LLVM/build>/lib/cmake/llvm/ \
    ../fs-y2k38-checker
```

Run make inside the build directory.

```sh
make
```

This produces standalone tools called `bin/print-functions` and
`bin/runstreamchecker`. Loadable plugin variants of the analyses are also
produced inside `lib/`.

Note, building with a tool like ninja can be done by adding `-G Ninja` to
the cmake invocation and running ninja instead of make.

## Running

Both the AST plugins and clang static analyzer plugins can be run via standalone programs or via extra command line arguments to clang. The provided standalone variants can operate on individual files or on compilation databases, but compilation databases are somewhat easier to work with.

### AST Plugins

To load and run AST plugins dynamically in clang, you can use:

```sh
clang -fplugin=lib/libfunction-printer-plugin.so -c ../test/functions.c
```

To run the plugin via the standalone program:

```sh
bin/print-functions -- clang -c ../test/functions.c
```

Note that this will require you to put the paths to all headers in the command
line (using `-I`) or they will not be found. It can be simpler to instead use
a compilation database:

```sh
bin/print-functions -p compile_commands.json
```

### Clang Static Analyzer Plugins

To load and run a static analyzer plugin dynamically in clang, use:

```sh
clang -fsyntax-only -fplugin=lib/libstreamchecker.so \
    -Xclang -analyze -Xclang -analyzer-checker=demo.streamchecker \
    ../clang-plugins-demo/test/files.c
```

To run the plugin via the standalone program:

```sh
bin/runstreamchecker -- clang -c ../clang-plugins-demo/test/files.c
```

Again, missing headers are likely, and using a compilation database is the
preferred and simplest way to work around this issue. Note that clang comes
with scripts that can build a compilation database for an existing project.

## Detection items

| DONE | function | read/write (r/w) | st_atime / st_mtime / st_ctime (a/m/c) |
| ---- | -------- | ---------------- | -------------------------------------- |
| ⬜   | stat()   | r                | a,m,c                                  |
| ⬜   | lstat()  | r                | a,m,c                                  |
| ⬜   | fstat()  | r                | a,m,c                                  |
| ⬜   | utime()  | w                | a                                      |
| ⬜   | utimes() | w                | a                                      |
| ⬜   | creat()  | w                | a                                      |
| ⬜   | mknod()  | w                | a                                      |
| ⬜   | pipe()   | w                | a                                      |
| ⬜   | read()   | w                | a                                      |
| ⬜   | utime()  | w                | m                                      |
| ⬜   | utimes() | w                | m                                      |
| ⬜   | creat()  | w                | m                                      |
| ⬜   | mknod()  | w                | m                                      |
| ⬜   | pipe()   | w                | m                                      |
| ⬜   | write()  | w                | m                                      |
| ⬜   | ckmod()  | w                | c                                      |
| ⬜   | chown()  | w                | c                                      |
| ⬜   | creat()  | w                | c                                      |
| ⬜   | link()   | w                | c                                      |
| ⬜   | mkmod()  | w                | c                                      |
| ⬜   | pipe()   | w                | c                                      |
| ⬜   | unlink() | w                | c                                      |
| ⬜   | utime()  | w                | c                                      |
