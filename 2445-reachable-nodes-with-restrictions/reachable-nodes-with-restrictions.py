class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import deque
        count=1
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        q=deque([0])
        visited=[False]*n
        visited[0]=True
        rest=set(restricted)
        while q:
            for _ in range(len(q)):
                node=q.popleft()

                for nei in graph[node]:
                    if nei not in rest and not visited[nei]:
                        count+=1
                        visited[nei]=True
                        q.append(nei)
        return count
