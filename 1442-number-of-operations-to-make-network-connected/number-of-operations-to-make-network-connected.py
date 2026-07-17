class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        if len(edges) < n - 1:
            return -1
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n

        def dfs(node):
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        k=0
        for i in range(n):
            if not visited[i]:
                k+=1
                dfs(i)
        return k-1
        