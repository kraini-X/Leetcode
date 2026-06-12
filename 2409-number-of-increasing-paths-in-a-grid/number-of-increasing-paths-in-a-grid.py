class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        print(count)
        memo={}
        mod=10**9+7
        def solve(i,j,prev):
            
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            curr=grid[i][j]

            if grid[i][j]<=prev:
                return 0
            
            if (i,j,prev) in memo:
                return memo[(i,j,prev)]
            count=1

            count+=solve(i+1,j,curr)
            count+=solve(i-1,j,curr)
            count+=solve(i,j+1,curr)
            count+=solve(i,j-1,curr)
            memo[(i,j,prev)]=count
            return count

        for i in range(m):
            for j in range(n):
                count+=solve(i,j,-1)
        return count%mod
        



        