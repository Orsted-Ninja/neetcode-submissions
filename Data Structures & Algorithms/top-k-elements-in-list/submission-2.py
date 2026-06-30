class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=defaultdict(int)
        c=Counter(nums)
        x=[]
        y=sorted(c.items(),key=lambda x:x[1],reverse=True)
        for i in y:
            x.append(i[0])
            if len(x)==k:
                return x
