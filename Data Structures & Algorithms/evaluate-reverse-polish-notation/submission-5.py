class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = deque()

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                x.append(int(i))
            else:
                b = x.pop()
                a = x.pop()

                if i == '+':
                    x.append(a + b)
                elif i == '-':
                    x.append(a - b)
                elif i == '*':
                    x.append(a * b)
                elif i == '/':
                    x.append(int(a / b))

        return x[0]