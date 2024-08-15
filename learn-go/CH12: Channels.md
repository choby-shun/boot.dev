### Channels

#### Go routines

Go was designed to be concurrent, which is a trait fairly unique to Go. It excels at performing many tasks simultaneously safely using a simple syntax.

There isn't a popular programming language in existence where spawning concurrent execution is quite as elegant, at least in my opinion.

Concurrency is as simple as using the go keyword when calling a function:
```go
go doSomething()
```

In the example  above, `doSomething()` will be executed concurrently with the rest of the program. The `go` keyword is used to spawn a new goroutine.

#### Channels

Channels are typed, thread-safe queue. Channels allow different goroutines to communicate with each other.

Create a channel:
```go
ch := make(chan int)
```

Send data to a channel:
```go
ch <- 42
```
The `<-` operator is called the `channel operator`. Data flows in the direction of the arrow. This operation will block until another goroutine is ready to receive the value.

#### Receive data from a channel
```go
v := <-ch
```
This reads and removes a value from the channel and saves it into the variable `v`. This operation will block until there is a value in the channel to be read.

#### Blocking and Deadlocks
A deadlock is when a group of goroutines are blocking so none of them can continue. This is a common bug that you need to watch out for in concurrent programming.
```

Empty structs are often used as a unary value. Sometimes, we don't care what is passed through a channel. We care when and if it is passed. This is a common pattern in Go.
We can block and wait until something is sent on a channel using the following syntax:
```go
<-ch
```

This will block until it pops a single item off the channel, then continue, discarding the item.


#### Buffered Channels

Creating a channel with a Buffer:
```go
ch := make(chan int, 10)
```

A buffer allows the channel to hold a fixed number of values before sending blocks. This means sending on a buffered channel only blocks when the buffer is full, and receiving blocks only when the buffer is empty.

Closing isn't necessary. 

#### Closing Channels

Channels can be explicitly closed using the `close()` function. This is useful when you have a receiver that needs to know when there are no more values coming through the channel.

```go
ch := make(chan int)

// do something

close(ch)
```

Check if a channel is closed:

```go
v, ok:= <-ch

// ok is `false` if the channel is closed
```

Do not send on a closed channel. Sending on a closed channel will cause a panic. A panic on the main goroutine will cause the entire program to crash, and a panic in any other gorouthine will case that goroutine to crash.

#### Range Over Channels

```go
for item := range ch {
  // do something
}
```

#### Select

Sometimes we have a single goroutine listening to multiple channels, and want to process data in the order it comes through each channel. A `select` statement is used to listen to multiple channels at the same time. It is similar to a `switch` statement but for channels.

```go
select {
case i, ok := <-chInts:
  // do something
case s, ok := <-chStrings:
  // do something
}
```

The first channel with a value ready to be received will fire and its body will executed. If multiple channels are ready, one will be chosen at random.
The `ok`  varialble in the example above refers to whether or not the channel has been closed by the sender yet. 

The `default` case is executed if no channels are ready to be received. It can stop the select statement from blocking.


- `time.Tick()` is a standard library function that returns a channel that sends a value on a given interval.
- `time.After()` sends a value once after the duration has passed.
- `time.Sleep()` blocks the current goroutine for the specified amount of time.

#### Readonly and Writeonly Channels
A channel can be declared as read-only or write-only by specifying the direction of the channel when declaring it.
```go
func main () {
  ch := make(chan int)
  readCh(ch)
}

func readCh(ch <-chan int) {
  // do something
}
```

```go
func writeCh(ch chan<- int) {
  // do something
}
```


A send to a nil channel blocks forever

```go
var c chan string // c is nil
c <- "let's get started" // blocks
```

A receive from a nil channel blocks forever
```go
var c chan string // c is nil
fmt.Println(<-c) // blocks
```

A send to a closed channel panics

```go
var c = make(chan int, 100)
close(c)
c <- 1 // panic: send on closed channel
```

A receive from a closed channel returns the zero value immediately
```go
var c = make(chan int, 100)
close(c)
fmt.Println(<-c) // 0
```
