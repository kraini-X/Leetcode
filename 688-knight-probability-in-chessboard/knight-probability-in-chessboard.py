class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]
        dp=[[[-1]*(k+1) for _ in range(n+1)] for _ in range(n+1)]
        def solve(i,j,mv):
            
            
            if i<0 or i>=n or j<0 or j>=n:
                return 0
            if mv==0:
                return 1
            if dp[i][j][mv]!=-1:
                return dp[i][j][mv]
            prob=0
            ans=0

            for dr,dc in dirs:
                nr=i+dr
                nc=j+dc

                ans+=1/8*solve(nr,nc,mv-1)
            dp[i][j][mv]=ans
            return ans
        return solve(row,column,k)

