# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def is_leaf(node:Optional[TreeNode]):
            return  (not node.left and not node.right)

        def pre_order_dfs(node:Optional[TreeNode], path:List[str]):
            if(not node):
                return 

            path.append(str(node.val))
            #append the node to the memo
            if(is_leaf(node)):
                result.append("->".join(path))
            else:
                #go left
                pre_order_dfs(node.left, path)
                #go right
                pre_order_dfs(node.right, path)

            path.pop()
            
        pre_order_dfs(root, [])

        return result