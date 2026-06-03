class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dirs=[(1, - 1),(1, 0),(1, 1)]
        dp=[[[-1]*(n+1) for _ in range(n+1)] for _ in range(m+1)]
        def solve(r,c1,c2):
            if c1<0 or c1>=n or c2<0 or c2>=n or r<0 or r>=m:
                return 0 
            if dp[r][c1][c2]!=-1:
                return dp[r][c1][c2]

            cherries=0
            if c1==c2:
                cherries=grid[r][c1]
            else:
                cherries=grid[r][c1]+grid[r][c2]
            
            if r==m-1:
                return cherries
            ans=0
            for dr1,dc1 in dirs:
                for dr2,dc2 in dirs:
                    ans=max(ans,solve(r+1,c1+dc1,c2+dc2))
            dp[r][c1][c2]=ans+cherries
            return ans+cherries
        return solve(0,0,n-1)
            
        