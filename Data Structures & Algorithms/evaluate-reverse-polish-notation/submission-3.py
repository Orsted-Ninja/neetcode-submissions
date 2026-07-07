class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x=deque()
        for i in tokens:
            if i not in ['+','-','*','/']:
                x.append(int(i))
            else:
                b=x.pop()
                a=x.pop()
                if i=='+':
                    x.append(int(b+a))
                if i=='-':
                    x.append(int(b-a))
                if i=='*':
                    x.append(int(b*a))
                if i=='/':
                    if a==0:continue
                    x.append(int(b//a))
        return x[0]
