class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque
        m=len(grid)
        n=len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    fresh+=1

        time=0

        while q and fresh!=0:
            for _ in range(len(q)):

                r,c=q.popleft()

                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc

                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append([nr,nc])
            time+=1
        if fresh==0:
            return time
        return -1
                
