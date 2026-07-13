class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]>5:return False
        s=0

        for i in bills:
            if i>5:
                if (s-(i-5))<0:return False
                else:s-=i
            s+=i

        return True

        