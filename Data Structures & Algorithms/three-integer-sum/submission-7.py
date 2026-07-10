class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:continue
            l=i+1
            r=len(nums)-1
            while l<r:
                z=nums[i]+nums[l]+nums[r]
                j=[nums[i],nums[l],nums[r]]
                if z==0 and j not in s:s.append(j)
                elif z<0:
                    l+=1
                else :
                    r-=1
        return s
                
        