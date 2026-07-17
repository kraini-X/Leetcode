class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n=len(grid)
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        minTime=[[float('inf')]*n for _ in range(n)]
        minTime[0][0]=0
        pq=[(grid[0][0],0,0)]

        while pq:
            time,r,c=heapq.heappop(pq)

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<n:
                    newTime=max(time,grid[nr][nc])
                    if newTime<minTime[nr][nc]:
                        minTime[nr][nc]=newTime
                        heapq.heappush(pq,(newTime,nr,nc))
        return minTime[n-1][n-1]


