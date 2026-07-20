class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        c=Counter(nums)
        for i,v in c.items():
            if v>1:
                return i
        return None
        