class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        visited=[[False]*n for _ in range(m)]
        def dfs(r,c):
            #if r<0 or r>m or c<0 or c>n:
                #return
            if r==m-1 and c==n-1:
                return True
            visited[r][c]=True

            if grid[r][c]==1:
                if 0<=r<m and 0<=c-1<n and grid[r][c-1] in [1,4,6]:
                    if not visited[r][c-1]:
                        if dfs(r,c-1):
                            return True
                if 0<=r<m and 0<=c+1<n and grid[r][c+1] in [1,3,5]:
                    if not visited[r][c+1]:
                        if dfs(r,c+1):
                            return True

            elif grid[r][c]==2:
                if 0<=r-1<m and 0<=c<n and grid[r-1][c] in [2,3,4]:
                    if not visited[r-1][c]:
                        if dfs(r-1,c):
                            return True
                if 0<=r+1<m and 0<=c<n and grid[r+1][c] in [2,5,6]:
                    if not visited[r+1][c]:
                        if dfs(r+1,c):
                            return True
                    
            elif grid[r][c]==3:
                if 0<=r<m and 0<=c-1<n and grid[r][c-1] in [6,4,1]:
                    if not visited[r][c-1]:
                        if dfs(r,c-1):
                            return True
                if 0<=r+1<m and 0<=c<n and grid[r+1][c] in [5,6,2]:
                    if not visited[r+1][c]:
                        if dfs(r+1,c):
                            return True
            elif grid[r][c]==4:
                if 0<=r<m and 0<=c+1<n and grid[r][c+1] in [5,3,1]:
                    if not visited[r][c+1]:
                        if dfs(r,c+1):
                            return True
                if 0<=r+1<m and 0<=c<n and grid[r+1][c] in [5,2,6]:
                    if not visited[r+1][c]:
                        if dfs(r+1,c):
                            return True
            elif grid[r][c]==5:
                if 0<=r-1<m and 0<=c<n and grid[r-1][c] in [3,4,2]:
                    if not visited[r-1][c]:
                        if dfs(r-1,c):
                            return True
                if 0<=r<m and 0<=c-1<n and grid[r][c-1] in [6,1,4]:
                    if not visited[r][c-1]:
                        if dfs(r,c-1):
                            return True

            elif grid[r][c]==6:
                if 0<=r<m and 0<=c+1<n and grid[r][c+1] in [5,1,3]:
                    if not visited[r][c+1]:
                        if dfs(r,c+1):
                            return True
                if 0<=r-1<m and 0<=c<n and grid[r-1][c] in [3,2,4]:
                    if not visited[r-1][c]:
                        if dfs(r-1,c):
                            return True
            return False
        return dfs(0,0)


