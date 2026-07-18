class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        z={}
        l,res=0,0
        for i in range(len(s)):
            if s[i] in z:
                l=max(l,z[s[i]]+1)
            z[s[i]]=i
            res=max(i-l+1,res)
        return res    