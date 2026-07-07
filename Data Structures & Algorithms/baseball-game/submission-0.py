class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []

        for op in operations:
            if op == "C":
                x.pop()
            elif op == "D":
                x.append(2 * x[-1])
            elif op == "+":
                x.append(x[-1] + x[-2])
            else:
                x.append(int(op))

        return sum(x)