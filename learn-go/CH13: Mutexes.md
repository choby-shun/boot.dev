### Mutexes

Mutexes in Go allow us to `lock` access to data. This ensures that we can control which goroutines can access certain data at which time.

Go's standard library provides a built-in implementation of mutex with the `sync.Mutex` type and its two methods: `Lock()` and `Unlock()`.


We can protect a block of code by surrounding it with a call to `Lock` and `Unlock` as shown on the protected method below.

It is a good practice to defer the `Unlock` call to ensure that the mutex is unlocked even if an error occurs.

```go
package main

import (
	"fmt"
	"sync"
)

type SafeMap struct {
	mu sync.Mutex
	m  map[string]int
}

func (sm *SafeMap) Get(key string) (int, bool) {
	sm.mu.Lock()         // Lock the mutex before accessing the map
	defer sm.mu.Unlock() // Unlock the mutex after the operation is complete

	value, ok := sm.m[key]
	return value, ok
}

func (sm *SafeMap) Set(key string, value int) {
	sm.mu.Lock()         // Lock the mutex before accessing the map
	defer sm.mu.Unlock() // Unlock the mutex after the operation is complete

	sm.m[key] = value
}

func main() {
	sm := SafeMap{
		m: make(map[string]int),
	}

	var wg sync.WaitGroup

	// Simulate concurrent writes
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			key := fmt.Sprintf("key%d", i)
			sm.Set(key, i)
			fmt.Printf("Set %s = %d\n", key, i)
		}(i)
	}

	// Simulate concurrent reads
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			key := fmt.Sprintf("key%d", i)
			value, ok := sm.Get(key)
			if ok {
				fmt.Printf("Get %s = %d\n", key, value)
			} else {
				fmt.Printf("Key %s not found\n", key)
			}
		}(i)
	}

	wg.Wait() // Wait for all goroutines to finish
}

```


#### Maps are not thread-safe

Maps are not thread safe for concurrent use. If there are multiple goroutines accessing a map, and at least one of them is writing to the map, we must `lock` the map with a `mutex`.

Note: sometimes, we run go programs on single threaded environment, such as web assembly, so the map is indeed thread safe. But in reality, Go code may or may not run on a single-core machine, so it's always best to write the code so that it is safe no matter which hardware it runs.

#### RW Mutex

The standard library also exposes a `sync.RWMutex`, it has these methods:
- RLock()
- RUnlock()

The `sync.RWMutex` can help with performance if we have a read-intensive process. Many goroutines can safely read from the map at the same time (multiple `RLock()` calls can happen simutaneously). However, only one goroutine can hold a `Lock()` and all `RLock()`'s will also be excluded.

```go
package main

import (
	"sync"
	"time"
)

type safeCounter struct {
	counts map[string]int
	mu     *sync.RWMutex
}

func (sc safeCounter) inc(key string) {
	sc.mu.Lock()
	defer sc.mu.Unlock()
	sc.slowIncrement(key)
}

func (sc safeCounter) val(key string) int {
	sc.mu.RLock()
	defer sc.mu.RUnlock()
	return sc.counts[key]
}

// don't touch below this line

func (sc safeCounter) slowIncrement(key string) {
	tempCounter := sc.counts[key]
	time.Sleep(time.Microsecond)
	tempCounter++
	sc.counts[key] = tempCounter
}
```


