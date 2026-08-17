class Solution:
    def stoneGameV(self,nums: List[int]) -> int:
        n=len(nums)
        leftSum=[0]*n
        rightSum=[0]*n
        leftSum[0]=nums[0]
        rightSum[n-1]=nums[n-1]

        for i in range(1,n):
            leftSum[i]=leftSum[i-1]+nums[i]
        
        for i in range(n-2,-1,-1):
            rightSum[i]=rightSum[i+1]+nums[i]
        
        dp = [[-1] * n for _ in range(n)]
        def solve(l,r):
            if l==r:
                return 0
            
            if dp[l][r]!=-1:
                return dp[l][r]
            ans=0
            leftOffset = leftSum[l - 1] if l > 0 else 0
            rightOffset = rightSum[r + 1] if r < n - 1 else 0

            for k in range(l, r):

                left = leftSum[k] - leftOffset
                right = rightSum[k + 1] - rightOffset
                if left>right:
                    ans=max(
                        ans,
                        right+solve(k+1,r)
                    )
                elif left<right:
                    ans=max(
                        ans,
                        left+solve(l,k)
                    )
                else:
                    ans=max(ans,
                    right+solve(k+1,r),
                    right+solve(l,k)
                    )
            dp[l][r]=ans
            return ans
        return solve(0,n-1)