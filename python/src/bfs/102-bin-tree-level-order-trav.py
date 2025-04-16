# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    #O(n*(l+r)) -> O(n^2)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        returns a list of elements representing the level order traversal of a tree
        """
        #bfs
        #use a dequeue for our queue
        #for each level, add each node to a result list
        # at the end of the level, add the list representing the level to the list
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        queue = deque([root])
        result = []
        #O(n) 
        while len(queue) > 0:
            level = []
            level_vals = []
            #O(l)
            while(len(queue) > 0):
                level.append(queue.popleft())
            #O(r)
            for val in level:
                level_vals.append(val.val)
                if(val.left is not None):
                    queue.append(val.left)
                if(val.right is not None):
                    queue.append(val.right)

            result.append(level_vals)
            
        return result
        
            