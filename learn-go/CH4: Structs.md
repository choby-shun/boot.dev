### Struct

`Struct` represents structured data, and it can be nested to represent more complex entities, the fields of struct can be accessed using `.` operator.
```go
type car struct {
  make string
  model string
  doors int
  mileage int
  frontWheel wheel
  backWheel wheel
}

type wheel struct {
  radius int
  material string
}

myCar := car{}
myCar.frontWheel.radius = 5
```
Go is not an object-oriented language. However, embedded `structs` provide a kind of data-only inheritance that can be useful at times. Go doesn't support classes or inheritance in the complete sense, but embedded `structs` are a way to elevate and share fields between `struct` definitions.

```go
type car struct {
  make string
  model string
}

type truck struct {
  // "car" is embedded, so the definition of a
  // "truck" now also additionally contains all
  // of the fields of the car struct
  car
  bedSize int
}
```

Embedded VS Nested
```go
lanesTruck := truck{
  bedSize: 10,
  car: car{
    make: "toyota",
    model: "camry",
  },
}

fmt.Println(lanesTruck.bedSize)

// embedded fields promoted to the top-level
// instead of lanesTruck.car.make
fmt.Println(lanesTruck.make)
fmt.Println(lanesTruck.model)
```

Struct methods in go
```go
type rect struct {
  width int
  height int
}

// area has a receiver of (r rect)
// rect is the struct
// r is the placeholder
func (r rect) area() int {
  return r.width * r.height
}

var r = rect{
  width: 5,
  height: 10,
}

fmt.Println(r.area())
// prints 50
```

Empty structs are used in Go as a unary value.

```go
// anonymous empty struct type
empty := struct{}{}

// named empty struct type
type emptyStruct struct{}
empty := emptyStruct{}
```

Syntax Example:
```go
package main

type membershipType string

const (
	TypeStandard membershipType = "standard"
	TypePremium  membershipType = "premium"
)

// don't touch above this line

type User struct {
	Membership 
	Name string
}

type Membership struct {
	Type membershipType
	MessageCharLimit int
}

func newUser(name string, membershipType membershipType) User {
	var charLimit int
	
	switch membershipType {
	case TypePremium: 
		charLimit = 1000
	default:
		charLimit = 100
	}
	user := User {
		Membership: Membership{
			Type: membershipType,
			MessageCharLimit: charLimit,
		},
		Name: name,
	}
	return user
}
```
