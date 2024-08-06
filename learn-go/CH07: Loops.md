### Loops in Go

The basic loop in Go is written in standard C-like syntax:

```go
for i := 0; i < 10; i++ {
  fmt.Println(i)
}
// Prints 0 through 9

```

Loops in Go can omit sections of a for loop. For example, the CONDITION (middle part) can be omitted which causes the loop to run forever.

```go
for INITIAL; ; AFTER {
  // do something forever
}
```

Most programming languages have a concept of a while loop. Because Go allows for the omission of sections of a for loop, a while loop is just a for loop that only has a CONDITION.

```go
plantHeight := 1

for plantHeight < 5 {
  fmt.Println("still growing! current height:", plantHeight)
  plantHeight++
}

fmt.Println("plant has grown to ", plantHeight, "inches")
```

The `continue` keyword stops the current iteration of a loop and continues to the next iteration. `continue` is a powerful way to use the `guard clause` pattern within loops.

```go
for i := 0; i < 10; i++ {
  if i % 2 == 0 {
    continue
  }
  fmt.Println(i)
}
// 1
// 3
// 5
// 7
// 9
```

The `break` keyword stops the current iteration of a loop and exits the loop

```go
for i := 0; i < 10; i++ {
  if i == 5 {
    break
  }
  fmt.Println(i)
}

// 0
// 1
// 2
// 3
// 4
```
