class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=[False]*n
        count=0
        def dfs(node):
            nonlocal count
            visited[node]=True
            sums=values[node]
            for nei in graph[node]:
                if not visited[nei]:
                    sums+=dfs(nei)
            if sums%k==0:
                    count+=1
                    return 0
            
            return sums
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return count

        