### Maps:

Maps are similar to JavaScript objects, Python dictionaries, and Ruby hashes. They store key-value pairs. 

The zero value of a map is `nil`.

```go
// Maps literal
ages := map[string]int{
  "alice": 25,
  "bob": 30,
}

// Maps make
ages:= make(map[string]int)
ages["alice"] = 25
ages["bob"] = 30
```

The `len()` function returns the number of key-value pairs in a map.

```go
ages := map[string]int{
  "alice": 25,
  "bob": 30,
}

fmt.Println(len(ages)) // 2
```

Basic operations on maps:
```go
// Insert or update an element in map m:
m[key] = elem

// Retrieve an element:
elem = m[key]

// Delete an element:
delete(m, key)

// Check if key is present:
elem, ok = m[key]
```

Any type can be used as a key in a map as long as the type supports the `==` operator. The language spec defines this precisely, but in short, comparable types are: boolean, numeric, string, pointer, channel, interface, and structs with comparable fields. Notably, slices, maps, and functions are not comparable.

Struct can be used to key data by creating a map of structs:
```go
type Key struct {
    Path, Country string
}

hits := make(map[Key]int)
hits[Key{Path: "/home", Country: "US"}] = 42

// Accessing the value
value := hits[Key{Path: "/home", Country: "US"}]
fmt.Println(value)  // Output: 42
```

In the example above, Key{Path: "/home", Country: "US"} is a new instance of the Key struct that is identical in content to the key already in the map. Go can successfully find and return the associated value because it compares the contents of the struct, not the memory address or reference.

In Python, dictionaries use object identity (i.e., the memory address) as the default basis for comparison when objects are used as keys. This means that two instances of a custom object, even if they contain the same data, will not necessarily be considered the same key unless the `__hash__` and `__eq__` methods are properly implemented to compare content rather than identity.

```python
class Key:
    def __init__(self, path, country):
        self.path = path
        self.country = country

    def __hash__(self):
        return hash((self.path, self.country))

    def __eq__(self, other):
        return (self.path, self.country) == (other.path, other.country)

# Create a dictionary with a custom object as the key
hits = {}
key1 = Key("/home", "US")
hits[key1] = 42

# Accessing the value with a new instance
key2 = Key("/home", "US")
value = hits[key2]  # Output: 42, but only if __hash__ and __eq__ are implemented
print(value)

```

- Go (Struct as Key): In Go, the comparison is based on the contents of the `struct`. Two `structs` with the same field values are considered equal, and they can be used interchangeably as keys in a map.

- Python (Object as Key): In Python, the default behavior is to compare objects by identity unless you override it with custom `__hash__` and `__eq__` methods to compare based on content.


#### Nested Maps

Maps can contain maps, creating a nested data structure. This is useful for representing hierarchical data.

```go
map[string]map[string]int
map[rune]map[string]int
map[int]map[string]map[string]int
```
