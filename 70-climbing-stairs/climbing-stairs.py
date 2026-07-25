class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def solve(pos):
            if pos>=n:
                return 1
            if dp[pos]!=-1:
                return dp[pos]
            single=solve(pos+1)
            double=solve(pos+2)
            dp[pos]=single+double
            return single+double
        return solve(1)
        