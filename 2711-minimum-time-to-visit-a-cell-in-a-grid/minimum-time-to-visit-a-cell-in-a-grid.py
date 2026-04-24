class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq
        m=len(grid)
        n=len(grid[0])
        minDist=[[float('inf')]*n for _ in range(m)]
        minDist[0][0]=0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        pq=[(0,0,0)]
        if m > 1 and n > 1 and grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        while pq:
            t,r,c=heapq.heappop(pq)

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n:
                    new=0
                    if t>=grid[nr][nc]:
                        new=t+1
                    if t<grid[nr][nc]:
                        diff=grid[nr][nc]-t
                        if diff%2==0:
                            new=grid[nr][nc]+1
                        else:
                            new=grid[nr][nc]
                    if new<minDist[nr][nc]:
                        minDist[nr][nc]=new
                        heapq.heappush(pq,(new,nr,nc))
        return minDist[m-1][n-1]



        