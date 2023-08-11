def evaluate_rpn(expression):
    stack = []

    for token in expression:
        if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):  # 数値をスタックに追加
            stack.append(int(token))
        else:
            b = stack.pop()  # スタックから2つの数値を取り出す
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # 除算の結果を整数とする

    return stack[0]  # 最終的な計算結果を返す


# テスト
# RPN式の例：3 4 + 5 *
expression = ["3", "4", "+", "5", "*"]
result = evaluate_rpn(expression)
print("Result:", result)  # 出力: 35
