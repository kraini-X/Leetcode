class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        suffix=[0]*n
        suffix[n-1]=piles[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=piles[i]+suffix[i+1]
        
        memo={}
        def solve(i,M):
            ans=float('-inf')
            if i>=n:
                return 0

            if i+2*M>=n:
                return suffix[i]
            if (i,M) in memo:
                return memo[(i,M)]
            for X in range(1,2*M+1):
                ans=max(
                    ans,
                    suffix[i]-solve(i+X,max(M,X))
                )
            memo[(i,M)]=ans
            return ans
        return solve(0,1)



