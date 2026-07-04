class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        n=len(nums)
        b=[]
        for i,v in a.items():
            if v>n/3:
                b.append(i)
        return b
        
        