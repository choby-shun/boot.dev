### Packages and Modules

By convention, a package's name is the same as the last element of the import path. For instance, the package `math/rand` comprises files that begin with the statement `package rand`.

A directory of Go code can have at most one package. All .go files in a single directory must all belong to the same package. If they don't, an error will be thrown by the compiler. This is true for main and library packages alike.

Go programs are organized into packages. A package is a directory of Go code that's all compiled together. Functions, types, variables, and constants defined in one source file are visible to all other source files within the same package (directory).

A repository contains one or more modules. A module is a collection of Go packages that are released together.

An "import path" is a string used to import a package. A package's import path is its module path joined with its subdirectory within the module. For example, the module `github.com/google/go-cmp` contains a package in the directory `cmp/`. That package's import path is `github.com/google/go-cmp/cmp`. Packages in the standard library do not have a module path prefix.


- You will have many git repositories on your machine (typically one per project).
- Each repository contains one or more packages
- Each repository is typically a single module.
- Each package consists of one or more Go source files in a single directory.

The `go build command` compiles go code into a single, statically linked executable program. One of the beauties of Go is that you always go build for production, and because the output is a statically compiled binary, you can ship it to production or end users without them needing the Go toolchain installed.

Some new Go devs use go run on a server in production, which is a huge mistake.

The `go install command` compiles and installs a package or packages on your local machine for your personal usage. It installs the package's compiled binary in the GOBIN directory.
