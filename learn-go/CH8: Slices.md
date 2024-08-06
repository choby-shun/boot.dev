### Array:

Arrays are fixed-size groups of variables of the same type.

```go
var myInts [10]int
primes := [6]int{2, 3, 5, 7, 11, 13}
```

99 times out of 100 you will use a slice instead of an array when working with ordered lists.

Arrays are fixed in size. Once you make an array like `[10]int` you can't add an 11th element.

A slice is a dynamically-sized, flexible view of the elements of an array.

The zero value of slice is `nil`.

Slices always have an underlying `array`, though it isn't always specified explicitly. To explicitly create a slice on top of an array we can do:

```go
primes := [6]int{2, 3, 5, 7, 11, 13}
mySlice := primes[1:4]
// mySlice = {3, 5, 7}
```

The syntas is:
```go
arrayname[lowIndex:highIndex]
arrayname[lowIndex:]
arrayname[:highIndex]
arrayname[:]
```

Where `lowIndex` is inclusive and `highIndex` is exclusive.

`lowIndex`, `highIndex`, or both can be omitted to use the entire array on that side of the colon.

Most of the time we don't need to think about the underlying array of a slice. We can create a new slice using the make function:

```go
// func make([]T, len, cap) []T
mySlice := make([]int, 5, 10)

// the capacity argument is usually omitted and defaults to the length
mySlice := make([]int, 5)
```

If we want to create a slice with a specific set of values, we can use a slice literal:

```go
mySlice := []string{"i", "love", "go"}
```

#### Length
The length of a slice is simply the number of elements it contains. It is accessed using the built-in `len()` function:

```go
mySlice := []string{"I", "love", "go"}
fmt.Println(len(mySlice)) // 3
```
The capacity of a slice is the number of elements in the underlying array, counting from the first element in the slice. It is accessed using the built-in `cap()` function:
```go
mySlice := []string{"I", "love", "go"}
fmt.Println(cap(mySlice)) // 3
```
Generally speaking, unless you're hyper-optimizing the memory usage of your program, you don't need to worry about the capacity of a slice because it will automatically grow as needed.


#### Variadic
Many functions, especially those in the standard library, can take an arbitrary number of final arguments. This is accomplished by using the "..." syntax in the function signature.

A variadic function receives the variadic arguments as a `slice`.

```go
func concat(strs ...string) string {
    final := ""
    // strs is just a slice of strings
    for i := 0; i < len(strs); i++ {
        final += strs[i]
    }
    return final
}

func main() {
    final := concat("Hello ", "there ", "friend!")
    fmt.Println(final)
    // Output: Hello there friend!
}
```

The familiar `fmt.Println()` and `fmt.Sprintf()` are variadic! fmt.Println() prints each element with space delimiters and a newline at the end.

#### SPREAD OPERATOR
The spread operator allows us to pass a slice into a variadic function. The spread operator consists of three dots following the slice in the function call.

```go
func printStrings(strings ...string) {
	for i := 0; i < len(strings); i++ {
		fmt.Println(strings[i])
	}
}

func main() {
    names := []string{"bob", "sue", "alice"}
    printStrings(names...)
}
```

#### Append

The built-in append function is used to dynamically add **elements** to a slice:

```go
func append(slice []Type, elems ...Type) []Type
```

If the underlying array is not large enough, `append()` will create a new underlying array and point the slice to it.

Notice that `append()` is `variadic`, the following are all valid:
```go
slice = append(slice, oneThing)
slice = append(slice, firstThing, secondThing)
slice = append(slice, anotherSlice...)
```

#### Slice of Slices

Slices can hold other slices, effectively creating a `matrix`, or a 2D array.
```go
rows := [][]int{
    []int{1, 2, 3},
    []int{4, 5, 6},
    []int{7, 8, 9},
}

// Create matrix with value for each cell is the product of the row and column index
package main

func createMatrix(rows, cols int) [][]int {
	matrix := [][]int{}

	for i := 0; i < rows; i++ {
		row := []int{}
		for j := 0; j < cols; j++ {
			row = append(row, i*j)
		}
		matrix = append(matrix, row)
	}

	return matrix
}

```

#### Range

Go provides syntactic sugar for looping over slices and maps. The `range` keyword is used to iterate over a slice or map.
```go
for INDEX, ELEMENT := range SLICE {
    // do something with INDEX and ELEMENT
}

fruits := []string{"apple", "banana", "grape"}
for i, fruit := range fruits {
    fmt.Println(i, fruit)
}
// 0 apple
// 1 banana
// 2 grape
```
