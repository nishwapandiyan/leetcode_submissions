# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,cur):
            if root is None:
                return 0
            cur = cur * 10 + root.val    
            if root.left is None and root.right is None:
                return cur
            return dfs(root.left,cur) + dfs(root.right,cur)
        return dfs(root,0)        
