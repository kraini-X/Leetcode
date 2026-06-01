class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        from functools import lru_cache
        n=len(nums)
        #dp=[[-1]*n for i in range(n)]
        @lru_cache(None)
        def solve(idx):
            if idx==n-1:
                return 0
            #if dp[idx][jmp]!=-1:
                #return dp[idx][jmp]
            res=float('-inf')
            for j in range(idx+1,n):
                if abs(nums[idx]-nums[j])<=target:
                    res=max(res,1+solve(j))
            #dp[idx][jmp]=res
            return res
        ans=solve(0)
        return  ans if ans!=float('-inf') else -1

        