class Solution:
    def evaluatePostfix(self, arr):
        stack = []

        for ch in arr:
            if ch not in  {"+","-","*","/","^"}:
                stack.append(int(ch))
            else:
                a = stack.pop()
                b = stack.pop()

                if ch == "+":
                    stack.append(b + a)
                elif ch == "-":
                    stack.append(b - a)
                elif ch == "*":
                    stack.append(b * a)
                elif ch == "/":
                    stack.append(b // a)
                elif ch == "^":
                    stack.append(b ** a)

        return stack[-1]