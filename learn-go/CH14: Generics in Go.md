### Generics

Put simply, generics are a way to write code that works across different types. They allow you to write functions, data structures, and algorithms that are type-agnostic.

```go
func splitAnySlice[T any](s []T) ([]T, []T) {
  // Split the slice into two halves
  mid := len(s) / 2
  return s[:mid], s[mid:]
}

firstInts, secondInts := splitAnySlice([]int{0, 1, 2, 3})
fmt.Println(firstInts, secondInts)
```

zero value for generic types is `nil`

Sometimes you need the logic in your generic function to know something about the types it operates on.

Create a custom constraint:
```go
type stringer interface {
    String() string
}

func concat[T stringer](vals []T) string {
    result := ""
    for _, val := range vals {
        // this is where the .String() method
        // is used. That's why we need a more specific
        // constraint instead of the any constraint
        result += val.String()
    }
    return result
}
```
