class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for i in matrix:
            l=0
            r=len(i)-1
            while l<=r:
                mid=l+(r-l)//2
                if mid==target:
                    return True
                elif mid<target:
                    l=mid+1
                else:
                    r=mid-1
        return False
        
        