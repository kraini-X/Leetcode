class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,2*w))
        dist=[float('inf')]*n
        pq=[(0,0)]

        while pq:
            w,node=heapq.heappop(pq)

            for nei,n_w in graph[node]:
                if w+n_w<dist[nei]:
                    dist[nei]=w+n_w
                    heapq.heappush(pq,(w+n_w,nei))
        
        return dist[n-1] if dist[n-1]!=float('inf') else -1
        