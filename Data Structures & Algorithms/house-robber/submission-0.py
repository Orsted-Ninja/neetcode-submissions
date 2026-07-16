class Solution:
    def rob(self, nums: List[int]) -> int:
        p2=nums[0]
        p1=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            curr=max(p1,p2+nums[i])
            p2=p1
            p1=curr
        return p1