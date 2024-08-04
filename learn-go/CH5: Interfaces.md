### Interfaces

Interfaces are just collections of method **signatures**. A type "implements" an interface if it has methods that match the interface's method signatures.

```go
type shape interface {
  area() float64
  perimeter() float64
}

type rect struct {
    width, height float64
}
func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perimeter() float64 {
    return 2*r.width + 2*r.height
}

type circle struct {
    radius float64
}
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perimeter() float64 {
    return 2 * math.Pi * c.radius
}
```

A type never declares that it implements a given interface. If an interface exists and a type has the proper methods defined, then the type automatically fulfills that interface.

Implicit interfaces decouple the definition of an interface from its implementation. You may add methods to a type and in the process be unknowingly implementing various interfaces, and that's okay.

Better define `interface` with argument name
```go
type Copier interface {
  Copy(sourceFile string, destinationFile string) (bytesCopied int)
}
```

A type switch makes it easy to do several type assertions in a series.

A type switch is similar to a regular switch statement, but the cases specify types instead of values.

```go
func printNumericValue(num interface{}) {
	switch v := num.(type) {
	case int:
		fmt.Printf("%T\n", v)
	case string:
		fmt.Printf("%T\n", v)
	default:
		fmt.Printf("%T\n", v)
	}
}

func main() {
	printNumericValue(1)
	// prints "int"

	printNumericValue("1")
	// prints "string"

	printNumericValue(struct{}{})
	// prints "struct {}"
}
```

Some notes:
1. KEEP INTERFACES SMALL

If there is only one piece of advice that you take away from this article, make it this: keep interfaces small! Interfaces are meant to define the minimal behavior necessary to accurately represent an idea or concept.

2. INTERFACES SHOULD HAVE NO KNOWLEDGE OF SATISFYING TYPES

An interface should define what is necessary for other types to classify as a member of that interface. They shouldn’t be aware of any types that happen to satisfy the interface at design time.

3. INTERFACES ARE NOT CLASSES

Interfaces are not classes, they are slimmer.
Interfaces don’t have constructors or deconstructors that require that data is created or destroyed.
Interfaces aren’t hierarchical by nature, though there is syntactic sugar to create interfaces that happen to be supersets of other interfaces.
Interfaces define function signatures, but not underlying behavior. Making an interface often won’t DRY up your code in regards to struct methods. For example, if five types satisfy the fmt.Stringer interface, they all need their own version of the String() function.
