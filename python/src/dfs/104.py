# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if (not root.left and not root.right):
            return 1
        #dfs 
        def dfs(root):
            #if leaf, return 0
            if not root:
                return 0
            nonlocal maximum#read nonlocal var we will use to track max
            return max(maximum, 1 + dfs(root.left), 1 + dfs(root.right))
        maximum = 1
        return dfs(root) 
        
