class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                x=nums[i]+nums[l]+nums[r]
                if x==0:
                    s.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif x<0:
                    l+=1
                else:r-=1
        return s


            



        


        