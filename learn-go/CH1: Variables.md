### Basic Variables in Go

- `bool`: either `true` or `false`
- `string`: a sequence of characters
- `int`: a signed integer
- `float64`: a floating point number
- `byte`: 8 bits of data

### Declaring Variables
```go
// Sad variable declaration
var mySkillIssues int // Declaring a variable, and default value is 0
mySkillIssues = 10

// Happy variable declaration
// type inference or type is inferred with walrus operator
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

### WHAT'S THE DEAL WITH THE SIZES?
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
