### Pointers

When we assign a value to a variable, we are storing that value in a specific memory location. We can access this memory location using the `&` operator. This operator returns the memory address of the variable. This memory address is called a `pointer`.

```go
x := 10

var p *int = &x

*p = 20

fmt.Println(x) // 20
```

It's possible to define an empty pointer. Its zero value is `nil`, which means it doesn't point to any memory address.

It's common to immediately create a new pointer by instead using the `&` operator to get a pointer to its operand:

```go
myString := "Hello, World!"
myStringPointer := &myString
```

#### Dereference

The `*` operator dereferences a pointer to get the original value.

```go
fmt.Println(*myStringPointer) // Hello, World!
*myStringPointer = "Hello, Go!"
```
```

Unlike C, Go has no pointer arithmetic. This means we can't increment or decrement a pointer. We can only get the address of a variable and dereference it.
