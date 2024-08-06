### Functions:

Syntax:

```go
func sub(x int, y int) int {
  return x - y
}
```
When multiple arguments are of the same type, and are next to each other in the function signature, the type only needs to be decalred after the last argument.
```go
func sub(x, y int) {
  // ...
}
```

Same as python, if we don't care the return value, we can explicitly ignore it by using an `underscore`, or more precisely, the `blank identifier`. 

The Go compiler will __throw an error__ if you have any unused variable declarations in the codes.

```go
func getPoint() (x int, y int) {
  return 3, 4
}

// ignore y value
x, _ := getPoint()
```

Early returns is always better
```go
func getInsuranceAmount(status insuranceStatus) int {
  if !status.hasInsurance(){
    return 1
  }
  if status.isTotaled(){
    return 10000
  }
  if !status.isDented(){
    return 0
  }
  if status.isBigDent(){
    return 270
  }
  return 160
}
```

Anonymous functions can be used to create quick `closure`
```go
func conversions(converter func(int) int, x, y, z int) (int, int, int) {
	convertedX := converter(x)
	convertedY := converter(y)
	convertedZ := converter(z)
	return convertedX, convertedY, convertedZ
}

func main() {
	newX, newY, newZ := conversions(func(a int) int {
	    return a + a
	}, 1, 2, 3)
	// newX is 2, newY is 4, newZ is 6

	newX, newY, newZ = conversions(func(a int) int {
	    return a * a
	}, 1, 2, 3)
	// newX is 1, newY is 4, newZ is 9
}
```

- `defer` keyword allows a function to be executed automatically __just__ before its enclosing function returns. The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding functions returns. It typically used to clean up resources that are no longer being used, like close database connections, file handlers.

Defer is a great way to make sure that something happens before a function exits, even if there are multiple return statements, a common occurrence in Go.

```go
GetUsername(dstName, srcName string) (user string, err error) {
  // Open a connection to a database
  conn, _ := db.Open(srcName)

  // Close the source file *anywhere* the GetUsername function returns
  defer conn.Close()

  username, err := db.FetchUser()
  if err != nil{
    // The defer statement is auto-executed if we return here
    return 0, err
  }

  // The defer statement is auto-executed if we return here
  return username, nil
}
```
Unlike `Python`, `Go` is not dunction-scoped, it's `block-scoped`. Variables declared inside a block are only accessible within that block (and its nested blocks). There's also the package scope.

It's a bit unusual, but occasionally you'll see a plain old explicit block. It exists for no other reason than to create a new scope.

```go
package main

func main() {
    {
        age := 19
        // this is okay
        fmt.Println(age)
    }

    // this is not okay
    // the age variable is out of scope
    fmt.Println(age)
}
```

`Closure` Example: 
```go
package main

func adder() func(int) int {
	number := 0

	return func(num int) int {
		number += num
		return number
	}
}
```

