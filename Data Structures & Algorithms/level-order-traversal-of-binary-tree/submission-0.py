# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        q=deque([root])
        x=[]
        
        while q:
            cur=len(q)
            cu=[]
            for _ in range(cur):
                a=q.popleft()
                cu.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            x.append(cu)
        return x



        
        
        