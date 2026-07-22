class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap={}
        for v,i in enumerate(numbers):
            x=target-i
            if x in hmap:
                return [hmap[x]+1,v+1]
            else:
                hmap[i]=v
        return []

        