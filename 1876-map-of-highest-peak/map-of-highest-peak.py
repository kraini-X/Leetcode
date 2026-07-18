class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        from collections import deque
        q=deque()
        m=len(grid)
        n=len(grid[0])
        ans=[[-1]*n for _ in range(m)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans[i][j]=0
                    q.append((i,j))
        
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()

                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and ans[nr][nc]==-1:
                        ans[nr][nc]=ans[r][c]+1
                        q.append((nr,nc))
        return ans
