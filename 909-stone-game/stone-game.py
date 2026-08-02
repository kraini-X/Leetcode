class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        memo={}
        def solve(i,j):
            if i > j:
                return 0

            if i==j:
                return piles[i]
            if (i,j) in memo:
                return memo[(i,j)]
            take_i = piles[i]+min(
                solve(i+2,j),solve(i+1,j-1)
            )

            take_j=piles[j]+ min(
                solve(i+1,j-1),solve(i,j-2)
            )
            memo[(i,j)]=max(take_i,take_j)
            return max(take_i,take_j)
        
        alice=solve(0,n-1)
        bob=sum(piles)-alice

        return alice>bob