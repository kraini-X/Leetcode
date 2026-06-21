class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
        m=len(labels)
        
        minCost=[[float('inf')]*(k+1) for _ in range(n)]
        minCost[0][1]=0
        pq=[(0,0,1)]

        while pq:
            w,node,streak=heapq.heappop(pq)

            if streak>k:
                continue
            if node == n - 1:
                return w
            
            for nei,wt in graph[node]:

                if labels[node]==labels[nei]:
                    new_streak=streak+1
                else:
                    new_streak=1
                if new_streak>k:
                    continue

                if w+wt<minCost[nei][new_streak]:
                    minCost[nei][new_streak]=w+wt
                    heapq.heappush(pq,(w+wt,nei,new_streak))
        return -1


            



        