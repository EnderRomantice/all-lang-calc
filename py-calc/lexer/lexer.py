TOKEN = {
    0: "EOF",
    1: "NUMBER",
    2: "PLUS",
    3: "MINUS",
    4: "MULTIPLY",
    5: "DIVIDE",
    6: "ERROR",
}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Lexer:
    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.cr = self.input[self.pos]

    def read_token(self) -> Token:
        self._read_space()

        is_num = []
        while self.cr is not None and "0" <= self.cr <= "9":
            is_num.append(self.cr)
            self._next_char()

        if is_num:
            return Token(TOKEN[1], int("".join(is_num)))

        match self.cr:
            case "+":
                self._next_char()
                return Token(TOKEN[2], "+")
            case "-":
                self._next_char()
                return Token(TOKEN[3], "-")
            case "*":
                self._next_char()
                return Token(TOKEN[4], "*")
            case "/":
                self._next_char()
                return Token(TOKEN[5], "/")
            case None:
                return Token(TOKEN[0], None)

            case _:
                bad = self.cr
                self._next_char()
                return Token(TOKEN[6], bad)

    def _read_space(self):
        while self.pos != len(self.input) - 1 and self.cr == " ":
            self._next_char()

    def _next_char(self):
        self.pos += 1

        if self.pos >= len(self.input):
            self.cr = None
            return

        self.cr = self.input[self.pos]
