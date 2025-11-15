from lexer.lexer import Lexer
from parser.parser import Parser

if __name__ == "__main__":
    input_exp = "1 + dddddddda2    awd * 3 +  awd    daw 4 / 5            "

    lexer = Lexer(input_exp)

    ast = Parser(lexer)

    ast.parse_expr()
