class Node:
    def __init__ (self,val:int = None, left = None, right = None):
        self.val = val
        self.right = right
        self.left=left

def dfs (n:Node):
    if(n is None):
        return None
    ##logic here
    return dfs(n.left) or dfs(n.right)