class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
        minCost=[[float('inf')]*(k+2) for _ in range(n)]
        minCost[src][0]=0
        
        graph=defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        pq=[(0,src,0)]
        while pq:
            price,node,stops=heapq.heappop(pq)
            
            if node==dst:
                return price
            
            if stops == k + 1:
                continue
                
            for nei,w in graph[node]:
                newPrice=price+w

                if newPrice<minCost[nei][stops+1]:
                    minCost[nei][stops+1]=newPrice
                    heapq.heappush(pq,(newPrice,nei,stops+1))
        return -1

        