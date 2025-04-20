# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #root to lead = pre order traversal
        #dfs using a path stack, recursion
        #result list
        result = []

        #only capture paths to leaves that sum to the target
        def dfs(node, path:list):
            if node is None:
                return 
            
            path.append(node.val)

            #save to result when leaf node = target
            if not node.left and not node.right and sum(path)==targetSum:
                result.append(path[:])
            
            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()


        dfs(root, [])
        return result
