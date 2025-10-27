package main

import (
	"fmt"
	"go-calc/token"
)

func main() {
	input := "12 + 34 - 5 * 6 / 3 aw"
	lexer := token.NewLexer(input)

	for tok := lexer.NextToken(); tok.Type != token.EOF; tok = lexer.NextToken() {
		fmt.Printf("%+v\n", tok)
	}
}
