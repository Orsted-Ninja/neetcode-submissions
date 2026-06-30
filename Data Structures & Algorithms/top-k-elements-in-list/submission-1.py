class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=defaultdict(int)
        c=Counter(nums)
        
        x=[]
        nums.sort()
        print(c)
        
        for i,v in c.items():
            print(i,v)
            if v>=k :
                x.append(i)
        x.sort(reverse=True)
        
        return x
        