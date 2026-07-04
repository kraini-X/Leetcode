class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        import heapq 
        from collections import defaultdict
        graph=defaultdict(list)
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        visited=[False]*(n+1)
        minm=float('inf')
        def dfs(node):
            nonlocal minm
            #if node==n:
                #return           
            visited[node]=True
            
            for nei,w in graph[node]:
                minm=min(minm,w)
                if not visited[nei]:
                    dfs(nei)
                    
        
        dfs(1)
        return minm



        