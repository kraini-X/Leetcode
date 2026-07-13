class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        n=len(grid)
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        visited = [[False] * n for _ in range(n)]
        q=deque([(0,0)])
        visited[0][0]=True
        level=1
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                if r==n-1 and c==n-1:
                    return level

                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]==0:
                        visited[nr][nc]=True
                        q.append((nr,nc))
            level+=1
        return -1



        