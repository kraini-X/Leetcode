"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldNew={}

        def dfs(node):
            if node in oldNew:
                return oldNew[node]
            
            copy=Node(node.val)
            oldNew[node]=copy

            for nei in node.neighbors:
                cloned_nei = dfs(nei)
                copy.neighbors.append(cloned_nei)

            return copy
        return dfs(node)        