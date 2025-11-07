from token.token import TOKEN, Lexer

if __name__ == "__main__":
    input_exp = input("input expression: ")

    lexer = Lexer(input_exp)

    while True:
        tk = lexer.readToken()
        if tk.type == TOKEN[0]:
            break
        print(f"type: {tk.type} value: {tk.value}")
