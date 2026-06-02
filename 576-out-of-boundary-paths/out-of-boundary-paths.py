class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp=[[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        mod=10**9+7
        def solve(i,j,moves):
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            ans=0

            if dp[i][j][moves]!=-1:
                return dp[i][j][moves]
            if moves>0:
                ans+=solve(i+1,j,moves-1)
                ans+=solve(i-1,j,moves-1)
                ans+=solve(i,j+1,moves-1)
                ans+=solve(i,j-1,moves-1)
            dp[i][j][moves]=ans
            return ans
        return solve(startRow,startColumn,maxMove)%mod
    
        