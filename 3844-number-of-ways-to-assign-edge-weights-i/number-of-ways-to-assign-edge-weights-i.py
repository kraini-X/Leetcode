class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph=defaultdict(list)
        mod=10**9+7
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        n=len(edges)
        visited=[False]*(n+2)
        maxDepth=0
        leaves=[]
        def dep(node,depth,visited):
            nonlocal maxDepth,leaves 
            maxDepth=max(maxDepth,depth)
            
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dep(nei,depth+1,visited)
        dep(1,0,visited)
        return 2**(maxDepth-1)%mod



        



        