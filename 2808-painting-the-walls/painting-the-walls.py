class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        def solve(idx,remaining):
            if remaining<=0:
                return 0
            if idx==n:
                return float('inf')           
            if dp[idx][remaining]!=-1:
                return dp[idx][remaining]
            notTake=solve(idx+1,remaining)
            take=cost[idx]+solve(idx+1,remaining-1-time[idx])
            
            dp[idx][remaining]=min(take,notTake)
            return min(take,notTake)
        return solve(0,n)

        