class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)

        
        visited=[False]*n
        def dfs(node):
            latest = float('-inf')
            earliest = float('inf')

            visited[node]=True
            if all(visited[nei] for nei in graph[node]):
                return baseTime[node]
            
            for nei in graph[node]:
                if not visited[nei]:
                    t=dfs(nei)
                    latest = max(latest, t)
                    earliest = min(earliest, t)
            ownDuration=(latest - earliest) + baseTime[node]
            return latest+ownDuration
        return dfs(0)
        