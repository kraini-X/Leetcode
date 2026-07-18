class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        from collections import defaultdict
        import heapq
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[0]=0
        dist[k]=0
        pq=[(0,k)]

        while pq:
            time,node=heapq.heappop(pq)

            for nei,t in graph[node]:
                newTime=time+t
                if newTime<dist[nei]:
                    dist[nei]=newTime
                    heapq.heappush(pq,(newTime,nei))
        print(dist)
        ans = max(dist[1:])

        if ans == float('inf'):
            return -1
        return ans