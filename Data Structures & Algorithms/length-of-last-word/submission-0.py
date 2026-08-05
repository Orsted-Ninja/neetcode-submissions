class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        a=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                a+=1
            else:
                return a

        