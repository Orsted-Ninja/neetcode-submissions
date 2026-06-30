
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if not nums:return []
        l,r,e=[],[],[]
        def sort(x):
            left,right,equal=[],[],[]
            if len(x)<=1:return x
            pivot=x[0]
            for i in x:
                if i==pivot:equal.append(i)
                elif i>pivot:right.append(i)
                else:left.append(i)    

                
            l=sort(left)
            r=sort(right)
            print(l,e,r)
            return l+equal+r
            print(l,e,r)
        return sort(nums)