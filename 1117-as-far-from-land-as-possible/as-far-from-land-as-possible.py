class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        m=len(grid)
        n=len(grid[0])
        q=deque()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
        visited=[[False]*(n) for _ in range(m)]
        maxm=float('-inf')
        dist = 0
        while q:
            dist+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==0:

                        grid[nr][nc]=1
                        q.append((nr,nc))
                        maxm=max(maxm,dist)
            
                            
        return maxm if maxm!=float('-inf') else -1

        
            
            