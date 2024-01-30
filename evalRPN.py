class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while len(tokens) > 0:
            toke = tokens.pop(0)
            if toke == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second + first)
            elif toke == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif toke == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)
            elif toke == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second) / first))
            else:
                stack.append(int(toke))
        return stack.pop()
