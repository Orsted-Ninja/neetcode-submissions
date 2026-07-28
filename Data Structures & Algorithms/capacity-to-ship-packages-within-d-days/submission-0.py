class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        def f(k,w,d):
            ship,cap=1,k
            for i in w:
                if cap-i<0:
                    ship+=1
                    if ship>days:return False
                    cap=k
                cap-=i
            return True

        while l<=r:
            mid=l+(r-l)//2
            if f(mid,weights,days):
                res=min(mid,res)
                r=mid-1
            else:
                l=mid+1
        return res

        