class Node:
    def __init__(self,val = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def bfs(root:Node):
    if n is None:
        return None
    
    queue = deque([root])
    while len(queue) > 0  :
        n = queue.popleft()
        queue.append(n.left)
        queue.append(n.right)
        if(True):
            return 
        #logic
    return None


def build_tree(nodes, f):
   val = next(nodes)
   if val == "x":
       return None
   left = build_tree(nodes, f)
   right = build_tree(nodes, f)
   return Node(f(val), left, right)

