package main

import (
	"syscall/js"
)

var Count int

func reset(this js.Value, args []js.Value) any {
	Count = 0
	document := js.Global().Get("document")
	document.Call("getElementById", "int").Set("innerHTML", Count)
	return 0
}

func inc(this js.Value, args []js.Value) any {
	Count = Count + 1

	document := js.Global().Get("document")
	document.Call("getElementById", "int").Set("innerHTML", Count)
	return 0

}
func dec(this js.Value, args []js.Value) any {
	Count = Count - 1
	document := js.Global().Get("document")
	document.Call("getElementById", "int").Set("innerHTML", Count)
	return 0
}

func main() {
	js.Global().Set("reset", js.FuncOf(reset))
	js.Global().Set("inc", js.FuncOf(inc))
	js.Global().Set("dec", js.FuncOf(dec))
	select {}

}
