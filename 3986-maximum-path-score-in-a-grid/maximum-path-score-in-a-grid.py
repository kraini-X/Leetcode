class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        costs={0:0,1:1,2:1}
        dp=[[[-1]*(k+1) for _ in range(n+1)]for _ in range(m+1)]
        def solve(i,j,cost):
            if i<0 or i>=m or j<0 or j>=n:
                return float('-inf')
            val=grid[i][j]
            score=val
            if cost<costs[val]:
                return float('-inf')

            if i==m-1 and j==n-1:
                if cost>=0:
                    return grid[i][j]
                           
            if dp[i][j][cost]!=-1:
                return dp[i][j][cost]
                
            score+=max(
                    solve(i+1,j,cost-costs[val]),solve(i,j+1,cost-costs[val])
            )
            dp[i][j][cost]=score
            return score
        res=solve(0,0,k)
        return  res if res!=float('-inf') else -1


        