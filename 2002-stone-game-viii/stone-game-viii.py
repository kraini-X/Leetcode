class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n=len(stones)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        memo={}
        def solve(i):
            if i==n-1:
                return prefix[n]
            if (i) in memo:
                return memo[(i)]
            take=prefix[i+1]-solve(i+1)
            skip=solve(i+1)
            memo[(i)]=max(take,skip)
            return max(take,skip)
        
        return solve(1)


        