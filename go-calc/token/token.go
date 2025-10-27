package token

type Token struct {
	Type    int
	Literal string
}

const (
	// iota 等同枚举
	ILLEGAL = iota // 未知或错误的字 (0)
	EOF            // 输入的结尾 (1)

	// 操作数
	NUMBER // (2)

	// 运算符
	PLUS     // +  (3)
	MINUS    // -  (4)
	ASTERISK // *  (5)
	SLASH    // /  (6)
)
