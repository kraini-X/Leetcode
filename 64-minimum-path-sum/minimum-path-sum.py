class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def solve(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return  float('inf')
            
            if i==m-1 and j==n-1:
                return grid[i][j]
            
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=grid[i][j]+min(
                solve(i+1,j),
                solve(i,j+1)
            )
            return grid[i][j]+min(
                solve(i+1,j),
                solve(i,j+1)
            )
        return solve(0,0)


        