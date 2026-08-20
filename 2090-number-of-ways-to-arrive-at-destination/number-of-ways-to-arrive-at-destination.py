class Solution:
    import heapq
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        dist=[float('inf')]*n
        ways=[0]*n
        dist[0]=0
        ways[0]=1
        pq=[(0,0)]

        while pq:
            curr_dist,u=heapq.heappop(pq)

            for v,d in graph[u]:
                new_dist=curr_dist+d

                if new_dist<dist[v]:
                    dist[v]=new_dist
                    ways[v]=ways[u]
                    heapq.heappush(pq,(new_dist,v))
                
                elif new_dist==dist[v]:
                    ways[v]+=ways[u]
        return ways[-1]%(10**9+7)

        

        