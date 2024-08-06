### Conditionals

- `if` statements in Go do not use parentheses around the condition:
```go
if height > 4 {
    fmt.Println("You are tall enough!")
}
```
- `else if` and `else` are supported
```go
if height > 6 {
    fmt.Println("You are super tall!")
} else if height > 4 {
    fmt.Println("You are tall enough!")
} else {
    fmt.Println("You are not tall enough!")
}
```

- We can define `variables` in the `if` initial statement, but the variables are created within the initial statement are only defined within the scope of `if` body

```go
if length := getLength(email); length < 1 {
    fmt.Println("Email is invalid")
}

//In the example above, length isn't available in the parent scope, which is nice because we don't need it there - we won't accidentally use it elsewhere in the function.
```

### Switch
- More concise and readable way when the number of options is more than 2
- Can use `fallthrough` keyword to fall through to the next `case`

```go
func getCreator(os string) string {
    var creator string
    switch os {
    case "linux":
        creator = "Linus Torvalds"
    case "windows":
        creator = "Bill Gates"

    // all three of these cases will set creator to "A Steve"
    case "Mac OS":
        fallthrough
    case "Mac OS X":
        fallthrough
    case "mac":
        creator = "A Steve"

    default:
        creator = "Unknown"
    }
    return creator
}
```

Go supports the standard `modulo operator`:
```go
7 % 3 // 1
```

The `AND` logical operator:
```go
true && false // false
true && true // true
```

As well as the `OR` operator
```go
true || false // true
false || false // false
```
