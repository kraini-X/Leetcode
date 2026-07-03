class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        import heapq
        graph=defaultdict(list)
        high=float('-inf')
        for u,v,w in edges:
            graph[u].append((v,w))
            high=max(high,w)
        
        def dijks(graph,mid,online):
            n = len(online)
            minCost=[float('inf')]*n
            minCost[0]=0
            pq=[(0,0)]

            while pq:
                wt,node=heapq.heappop(pq)
                if node==n-1:
                    return True
                if wt>minCost[node]:
                    continue
                for nei,nw in graph[node]:
                    if nw<mid:
                        continue
                    if not online[nei]:
                        continue
                    if nw+wt>k:
                        continue
                    
                    if nw+wt<minCost[nei]:
                        minCost[nei]=nw+wt
                        heapq.heappush(pq,(nw+wt,nei))
            return False
        
        low=0

        while low<=high:
            mid=(low+high)//2

            if dijks(graph,mid,online):
                low=mid+1
            else:
                high=mid-1
        return high if high>=0 else -1


        