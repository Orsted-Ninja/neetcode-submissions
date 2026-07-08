class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l=0
            r=len(i)-1
            while l<=r:
                mid=(l+r)//2
                if target==i[mid]:
                    return True
                elif target>i[mid]:l=mid+1
                else:r=mid-1
        return False
        