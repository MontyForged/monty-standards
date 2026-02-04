package main

import "fmt"

func hello(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}

func add(a, b int) int {
	return a + b
}

func main() {
	fmt.Println(hello("Go"))
}

// Tests
func TestHello(t *testing.T) {
	if hello("World") != "Hello, World!" {
		t.Error("hello test failed")
	}
}

func TestAdd(t *testing.T) {
	if add(2, 3) != 5 {
		t.Error("add test failed")
	}
}
