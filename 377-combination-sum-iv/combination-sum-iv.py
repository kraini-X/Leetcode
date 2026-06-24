class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[-1]*(target+1)
        def solve(rem):
            if rem<=0:
                return 1
            
            if dp[rem]!=-1:
                return dp[rem]
            ans=0
            for i in range(n):
                if nums[i]<=rem:
                    ans+=solve(rem-nums[i])
            dp[rem]=ans
            return ans

        return solve(target) 
        