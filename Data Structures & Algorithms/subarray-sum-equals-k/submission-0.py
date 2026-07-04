class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums)<k:
            return 0
        c=0
        fr=defaultdict(int)
        fr[0]=1
        pr=0
        for i in nums:
            pr+=nums
            if pr-k in fr:
                c+=freq[pr-k]
            fr[pr]+=1
        return c
                
            