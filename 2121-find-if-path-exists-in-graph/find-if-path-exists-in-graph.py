class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:
        from collections import deque
        q=deque()
        q.append(src)

        visited=[False]*n
        visited[src]=True

        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node==dest:
                    return True

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei]=True
                        q.append(nei)
        return False
        