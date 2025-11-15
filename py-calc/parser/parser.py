from lexer.lexer import TOKEN, Lexer, Token


class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer: Lexer = lexer
        self.cr_token: Token = lexer.read_token()

    def eat(self, type: int):
        if self.cr_token.type == TOKEN[type]:
            self.cr_token = self.lexer.read_token()
            return

        raise ValueError(f"Unexpected token: {self.cr_token}")

    def parse_expr(self):
        node = self.parse_term()

        while self.cr_token.type in (TOKEN[2], TOKEN[3]):
            op = self.cr_token
            self.eat(op.type)
            right = self.parse_term()
            node = Node(op.type, op.value, node, right)

        return node

    def parse_term(self):
        node = self.parse_factor()

        while self.cr_token.type in (TOKEN[4], TOKEN[5]):
            op = self.cr_token
            self.eat(op.type)
            right = self.parse_factor()
            node = Node(op.type, op.value, node, right)

        return node

    # just number
    def parse_factor(self):
        tk = self.cr_token
        if self.cr_token.type == TOKEN[1]:
            self.eat(1)
            return Node(TOKEN[1], tk)
