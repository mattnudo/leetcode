# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    #runtime: O(n) mem: O(1)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        #bfs queue, dfs stack(rec)
        #bfs for each node, flip l and r, then do in order traversal adding to queue
        #
        queue = deque([root])
        #while the queue is not empty
        while len(queue) > 0:
            node = queue.popleft()
            #invert l and r
            temp = node.left
            node.left = node.right
            node.right = temp
            #do not enqueue childless
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root