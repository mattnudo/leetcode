"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#https://algo.monster/liteproblems/133
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        A deep copy of the provided node's graph

        Parameters
        ------
        node : Optional['Node']
            a node in the graph

        returns
        ------
        Optional['Node'] : a deep copied node
        """
        # Dictionary to keep track of visited nodes and their clones.
        visited = {}

        def clone(node: 'Node') -> 'Node':
            """
            clone is a helper function which performs a depth-first traversal
            of the graph to create a deep copy of it.

            :param node: The graph node to be cloned
            :return: The cloned copy of the input node
            """
            if node is None:
                return None
                
            if node in visited:
                return visited[node]

            cloned = Node(node.val)
            visited[node] = cloned
            
            for neighbor in node.neighbors:
                cloned.neighbors.append(clone(neighbor)) 

            return cloned

        return clone(node)