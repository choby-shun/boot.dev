*** Error

An Error is any type that implements the simple built-in error interface:
```go
type error interface {
    Error() string
}

// Atoi converts a stringified number to an integer
i, err := strconv.Atoi("42b")
if err != nil {
    fmt.Println("couldn't convert:", err)
    // because "42b" isn't a valid integer, we print:
    // couldn't convert: strconv.Atoi: parsing "42b": invalid syntax
    // Note:
    // 'parsing "42b": invalid syntax' is returned by the .Error() method
    return
}
// if we get here, then
// i was converted successfully
```

A customized error interface:
Because errors are just interfaces, you can build your own custom types that implement the error interface. Here's an example of a userError struct that implements the error interface:
```go
type userError struct {
    name string
}

func (e userError) Error() string {
    return fmt.Sprintf("%v has a problem with their account", e.name)
}
```
It can then be used as an error:

```go
func sendSMS(msg, userName string) error {
    if !canSendToUser(userName) {
        return userError{name: userName}
    }
    ...
}
```

The Go standard library provides an "errors" package that makes it easy to deal with errors.

```go
package main

import (
	"errors"
)

func divide(x, y float64) (float64, error) {
	if y == 0 {
		return 0, errors.New("no dividing by 0")
	}
	return x / y, nil
}
```

The proper way to handle errors in Go is to make use of the error interface. Pass errors up the call stack, treating them as normal values. However, there is another way to deal with errors in Go: the panic function. When a function calls panic, the program crashes and prints a stack trace.

As a general rule, do not use panic!

The panic function yeets control out of the current function and up the call stack until it reaches a function that defers a recover. If no function calls recover, the goroutine (often the entire program) crashes.
```go
func enrichUser(userID string) User {
    user, err := getUser(userID)
    if err != nil {
        panic(err)
    }
    return user
}

func main() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("recovered from panic:", r)
        }
    }()

    // this panics, but the defer/recover block catches it
    // a truly astonishingly bad way to handle errors
    enrichUser("123")
}
```

If there is a truly unrecoverable error, one should use `log.Fatal` to print a message and exit the program.
