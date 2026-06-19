class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def solve(idx):
            if idx>=n:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            not_pick=solve(idx+1)
            pick=nums[idx]+solve(idx+2)
            dp[idx]=max(pick,not_pick)
            return max(pick,not_pick)
        return solve(0)




        