class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return []
        def sort(x):
            if len(x)<=1:
                return x
            l,r,e=[],[],[]
            pivot=nums[len(x)//2]
            for i in x:
                if i==pivot:e.append(i)
                elif i>pivot:r.append(i)
                else:l.append(i)
            l=sort(l)
            r=sort(r)
            return l+e+r
        nums[:]=sort(nums)
        print(nums)

        
        