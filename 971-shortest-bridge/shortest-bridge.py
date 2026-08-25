class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)

        q=deque()
        def island(r,c):
            if r<0 or r>=n or c<0 or c>=n:
                return

            if grid[r][c]==0:
                return
            grid[r][c]=0
            q.append((r,c))

            island(r+1,c)
            island(r-1,c)
            island(r,c+1)
            island(r,c-1)

        found=False
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    island(i,j)
                    found=True
                    break
            if found:
                break
        
        level=0
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                if grid[r][c]==1:
                    return level-1
                
                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc

                    if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            level+=1
        return -1

        