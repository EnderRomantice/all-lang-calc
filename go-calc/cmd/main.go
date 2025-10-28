package main

import (
	"fmt"
	"go-calc/lexer"
	"go-calc/parser"
)

func main() {
	input := "12 + 3 * 2 / 3 + 2/3 + 2 + 2 / 5 / 4 * 2"
	lexer := lexer.NewLexer(input)

	parser := parser.New(lexer)

	ast := parser.ParseExpression()

	fmt.Printf("Input: %s\n", input)
	fmt.Printf("AST: %v\n", ast.String())

}
