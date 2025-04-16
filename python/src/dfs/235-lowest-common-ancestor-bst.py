# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            return the lowest common ancestor of two nodes
        """
        if root is None:
            return None

        # If both n1 and n2 are smaller than root, 
        # go to left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both n1 and n2 are greater than root, 
        # go to right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If nodes n1 and n2 are on the opposite sides, 
        # root is the LCA
        return root