class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        from collections import defaultdict,deque
        graph=defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)
        res=[]
        for u,v in queries:
            graph[u].append(v)
            visited=[False]*n
            q=deque()
            q.append(0)
            visited[0]=True
            level=0
            while q:
                for _ in range(len(q)):
                    node=q.popleft()
                    #visited[node]=True

                    if node==n-1:
                        res.append(level)
                    
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei]=True
                            q.append(nei)
                level+=1
        return res



