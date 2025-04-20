# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Helper function to perform depth-first search
        def dfs(node: TreeNode) -> int:
            # Base case: if the current node is None, return 0
            if not node:
                return 0

            # Recursively calculate the maximum path sum on the left subtree
            # If negative, we take 0 to avoid decreasing the overall path sum
            left_max = max(0, dfs(node.left))
          
            # Similarly, do the same for the right subtree
            right_max = max(0, dfs(node.right))
          
            # Update the overall maximum path sum
            # This includes the node value and the maximum paths from both subtrees
            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, node.val + left_max + right_max)
          
            # Return the maximum path sum without splitting
            # The current node's value plus the greater of its left or right subtree paths
            return node.val + max(left_max, right_max)

        # Initialize the overall maximum path sum to negative infinity
        # To account for potentially all negative-valued trees
        max_path_sum = float('-inf')
      
        # Start DFS with the root of the tree
        dfs(root)
      
        # After DFS is done, max_path_sum holds the maximum path sum for the tree
        return max_path_sum
