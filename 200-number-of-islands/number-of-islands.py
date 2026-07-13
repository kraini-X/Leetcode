class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def solve(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]=="0":
                return
            grid[i][j]="0"
            solve(i+1,j)
            solve(i-1,j)
            solve(i,j+1)
            solve(i,j-1)

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    solve(i,j)
        return count

        