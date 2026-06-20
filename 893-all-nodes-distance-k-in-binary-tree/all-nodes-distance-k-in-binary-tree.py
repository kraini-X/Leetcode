# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res=[]

        graph=defaultdict(list)

        def build(node,parent):
            if not node:
                return
            
            if parent:
                graph[parent].append(node)
                graph[node].append(parent)
            
            build(node.left,node)
            build(node.right,node)
        
        build(root,None)
        visited=set()

        def dfs(node,depth):
            if not node:
                return
            
            if depth==k:
                res.append(node.val)
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei,depth+1)
        dfs(target,0)
        return res
                



            

            

        