class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums or not nums:
            return 1
        hmap=set()
        for i in nums:
            hmap.add(i)
        k=0
        for i in range(1,100000):
            if i in hmap:
                continue
            else:
                return i
            

        

        