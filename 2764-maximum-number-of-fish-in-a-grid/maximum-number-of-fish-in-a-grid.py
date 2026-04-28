class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return 0
            
            if grid[i][j]==0:
                return 0
            
            sums=grid[i][j]
            grid[i][j]=0
            sums+=dfs(i+1,j)
            sums+=dfs(i-1,j)
            sums+=dfs(i,j+1)
            sums+=dfs(i,j-1)

            return sums
        
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    ans=max(ans,dfs(i,j))
        return ans

        