class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
                return 0
        if len(nums)<=2:
                return max(nums)
        def pi(nums1):
            
            p2=nums1[0]
            p1=max(nums1[0],nums1[1])
            
            for i in range(2,len(nums1)):
                curr=max(p1,p2+nums1[i])
                p2=p1
                p1=curr
            return p1
        return max(pi(nums[1:]),pi(nums[:-1]))
            