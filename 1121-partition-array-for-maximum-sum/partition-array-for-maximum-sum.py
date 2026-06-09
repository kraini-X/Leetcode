class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n=len(arr)
        dp=[-1]*(n+1)
        def solve(idx):
            if idx==n:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            curr_sum=0
            maxm=float('-inf')
            for j in range(idx,min(n,idx+k)):
                maxm=max(maxm,arr[j])
                length=j-idx+1

                curr_sum=max(
                    curr_sum,
                    maxm*length+solve(j+1)

                )
                
            dp[idx]=curr_sum
            return curr_sum
        return solve(0)



        