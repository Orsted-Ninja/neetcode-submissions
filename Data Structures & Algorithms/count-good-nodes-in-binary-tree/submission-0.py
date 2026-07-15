# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        c=1

        
        if not root:return 0
        cur=root
        while cur and cur.left:
            c+=1
            cur=cur.left
            if not cur:
                if cur.right:
                    cur=cur.right
        return c




        