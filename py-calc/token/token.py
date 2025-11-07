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

    def readToken(self):
        self._readSpace()

        isNum = []
        while self.cr is not None and "0" <= self.cr <= "9":
            isNum.append(self.cr)
            self._nextChar()

        if isNum:
            return Token(TOKEN[1], int("".join(isNum)))

        match self.cr:
            case "+":
                self._nextChar()
                return Token(TOKEN[2], "+")
            case "-":
                self._nextChar()
                return Token(TOKEN[3], "-")
            case "*":
                self._nextChar()
                return Token(TOKEN[4], "*")
            case "/":
                self._nextChar()
                return Token(TOKEN[5], "/")
            case None:
                return Token(TOKEN[0], None)

            case _:
                bad = self.cr
                self._nextChar()
                return Token(TOKEN[6], bad)

    def _readSpace(self):
        while self.pos != len(self.input) - 1 and self.cr == " ":
            self._nextChar()

    def _nextChar(self):
        self.pos += 1

        if self.pos >= len(self.input):
            self.cr = None
            return

        self.cr = self.input[self.pos]
