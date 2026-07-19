class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 
        r=max(piles)
        res=r
        while l<=r:
            mid=l+(r-l)//2
            s=0
            for i in piles:
                s+=math.ceil(i/mid)
            if s<=h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
            
        