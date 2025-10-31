package parser

import (
	"fmt"
	"go-calc/lexer"
	"go-calc/token"
)

// 通用接口，用于调试
type Node interface {
	String() string
}

// 数字节点
type NumberNode struct {
	Value float64
}

func (n *NumberNode) String() string {
	return fmt.Sprintf("%g", n.Value)
}

// 二元运算节点
type BinaryNode struct {
	Op    token.Token
	Left  Node
	Right Node
}

func (bn *BinaryNode) String() string {
	return fmt.Sprintf("(%s %s %s)", bn.Left.String(), bn.Op.Literal, bn.Right.String())
}

// Parser 结构体
type Parser struct {
	lexer        *lexer.Lexer // 词法分析器实例
	currentToken token.Token  // 当前的 token
}

// 创建一个新的 Parser 实例
func New(l *lexer.Lexer) *Parser {
	p := &Parser{lexer: l}
	// 加载第一个 token
	p.nextToken()
	return p
}

// 前进到下一个 token
func (p *Parser) nextToken() {
	p.currentToken = p.lexer.NextToken()
}

// 解析的入口函数，构建整个表达式的 AST
func (p *Parser) ParseExpression() Node {
	// 从最低优先级的运算符开始解析（这里是加法和减法）
	return p.parseExpression(LOWEST)
}

// --- 运算符优先级定义 ---
const (
	_ int = iota
	LOWEST
	PLUS_MINUS     // +, -
	ASTERISK_SLASH // *, /
)

// 获取 token 对应的优先级
func (p *Parser) precedence(tok token.Token) int {
	switch tok.Type {
	case token.PLUS, token.MINUS:
		return PLUS_MINUS
	case token.ASTERISK, token.SLASH:
		return ASTERISK_SLASH
	default:
		return LOWEST
	}
}

// 核心解析函数
// precedence 是当前允许的最低优先级
func (p *Parser) parseExpression(precedence int) Node {
	// 1. 解析 "前缀" 部分
	left := p.parsePrefixExpression()

	// 2. 循环处理 "中缀" 部分
	// 只要当前 token 是运算符，并且其优先级高于我们传入的 precedence
	for p.currentToken.Type != token.EOF && p.precedence(p.currentToken) > precedence {
		// 解析中缀表达式
		left = p.parseInfixExpression(left)
	}

	return left
}

// 解析前缀表达式（目前只有数字）
func (p *Parser) parsePrefixExpression() Node {
	// 如果当前 token 是数字
	if p.currentToken.Type == token.NUMBER {
		node := &NumberNode{Value: parseFloat(p.currentToken.Literal)}
		p.nextToken() // 消费掉这个数字 token
		return node
	}
	// 其他情况
	return nil
}

// 解析中缀表达式
func (p *Parser) parseInfixExpression(left Node) Node {
	// 保存当前的运算符 token
	op := p.currentToken
	// 获取运算符的优先级
	precedence := p.precedence(op)

	p.nextToken() // 消费掉运算符 token

	// 递归地解析右侧表达式，传入当前运算符的优先级
	right := p.parseExpression(precedence)

	// 创建二元运算节点
	return &BinaryNode{Op: op, Left: left, Right: right}
}

func parseFloat(s string) float64 {
	var f float64
	fmt.Sscanf(s, "%f", &f)
	return f
}
