class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp={}
        def solve(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            
            if i==m-1 and j==n-1:
                return 1 if grid[i][j]==0 else 0
            
            if grid[i][j]==1:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            ans=0
            ans+=solve(i+1,j)
            ans+=solve(i,j+1)
            dp[(i,j)]=ans
            return ans
        return solve(0,0)
            

        