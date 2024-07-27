### Basic Variables in Go

- `bool`: either `true` or `false`
- `string`: a sequence of characters
- `int`: a signed integer
- `float64`: a floating point number
- `byte`: 8 bits of data

### Declaring Variables
```go
// Sad variable declaration
// Only way to define variables in package level
// Can not re-assign value within same scope, but can be used in nested scope
var mySkillIssues int // Declaring a variable, and default value is 0
mySkillIssues = 10
var mySkillIssues = 10

// Happy variable declaration
// type inference or type is inferred with walrus operator
// can only be used within functions (local scope)
mySkillIssues := 10 // Declaring a variable, and default value is 10
```

### Comments in Go
```go
// this is a single line comment

/*
  this is a multi-line comment
  spanning multiple lines
*/
```

### Type Size
Integers, uints, floats and complex numbers have fixed sizes in Go.

- Whole Numbers
```
int int8 int16 int32 int64
```

- Positive Whole Numbers
`uint` stands for unsigned integer
```
uint uint8 uint16 uint32 uint64 uintptr
```

- Signed Decimal Numbers
```
float32 float64
```

- Imaginary Numbers
```
complex64 complex128
```

### What's the Deal With the Sizes?
The size (8, 16, 32, 64, 128, etc) represents how many bits in memory will be used to store the variable. The "default" int and uint types refer to their respective 32 or 64-bit sizes depending on the environment of the user.

The "standard" sizes that should be used unless you have a specific performance need (e.g. using less memory) are:

- int
- uint
- byte
- rune
- float64
- complex128

### Converting Between Types
```go
temperature := 32.0
temperatureInt := int(temperature)
```

### Constants
Constants are declared with the const keyword. They can't use the `:=` short declaration syntax. Constants can be primitive types like strings, integers, booleans and floats. They can not be more complex types like slices, maps and structs.

However, `constants` can be computed as long as the computation can happen at compile time.
```go
const pi = 3.14159
```

### Formatting Strings in Go
- fmt.Printf - Prints a formatted string to standard out.
- fmt.Sprintf() - Returns the formatted string

#### Default Representation
```go
s := fmt.Sprintf("I am %v years old", 10)
// I am 10 years old

s := fmt.Sprintf("I am %v years old", "way too many")
// I am way too many years old
```

#### specific Representation
```go
// String
s := fmt.Sprintf("I am %s years old", "way too many")
// I am way too many years old

// Integer
s := fmt.Sprintf("I am %d years old", 10)
// I am 10 years old

// Float
s := fmt.Sprintf("I am %f years old", 10.523)
// I am 10.523000 years old

// The ".2" rounds the number to 2 decimal places
s := fmt.Sprintf("I am %.2f years old", 10.523)
// I am 10.52 years old
```
