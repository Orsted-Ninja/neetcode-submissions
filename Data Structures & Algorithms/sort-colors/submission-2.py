class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return []
        def sort(x):
            if len(x)<=1:
                return x
            l,r,e=[],[],[]
            pivot=x[len(x)//2]
            for i in x:
                if i==pivot:e.append(i)
                elif i>pivot:r.append(i)
                else:l.append(i)
            lr=sort(l)
            rr=sort(r)
            return lr+e+rr
        nums[:]=sort(nums)
        print(nums)

        
        