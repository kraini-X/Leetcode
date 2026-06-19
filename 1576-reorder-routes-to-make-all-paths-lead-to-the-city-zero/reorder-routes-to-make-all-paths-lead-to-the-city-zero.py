class Solution:
    def minReorder(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        directed=defaultdict(list)
        undirected=defaultdict(list)

        for u,v in edges:
            directed[u].append(v)
            undirected[u].append(v)
            undirected[v].append(u)
        visited=[False]*n
        count=0
        def dfs(node,parent):
            nonlocal count
            visited[node]=True
            for child in undirected[node]:
                if not visited[child]:
                    if child in directed[node]:
                        count+=1
                    dfs(child,node)
        dfs(0,-1)
        return count



        