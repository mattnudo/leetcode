# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #com: O(n), mem O(1)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # dfs trverses the tree and returns height
        # -1 means imbalanced
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left) 
            right = dfs(root.right) 

            if( left < 0 or right < 0 or abs(left - right) >1):
                return -1
            return 1 + max(left,right)

        if root is None:
                return True

        return dfs(root) >= 0