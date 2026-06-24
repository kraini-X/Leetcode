class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        def solve(idx,rem):

            if idx==n:
                return 1 if rem==0 else 0
            if (idx,rem) in memo:
                return memo[(idx,rem)]
            negative=solve(idx+1,rem+nums[idx])
            positive=solve(idx+1,rem-nums[idx])
            memo[(idx,rem)]=positive+negative
            return positive+negative
        return solve(0,target)
            
        