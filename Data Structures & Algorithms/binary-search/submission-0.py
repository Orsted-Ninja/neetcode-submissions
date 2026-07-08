class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        x=nums.copy()
        l=0
        r=len(x)-1
        
        while l<=r:
            mid=(l+r)//2
            if target==x[mid]:return mid
            elif target>x[mid]:l=mid+1
            else:r=mid-1
        return -1
        
        