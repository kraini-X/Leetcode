class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo={}
        def solve(i,remaining):
            if i==n:
                return 1 if remaining==0 else 0
            if (i,remaining) in memo:
                return memo[(i,remaining)]
            not_pick=solve(i+1,remaining)
            pick=0
            if coins[i]<=remaining:
                pick=solve(i,remaining-coins[i])
            memo[(i,remaining)]=pick+not_pick
            return pick+not_pick
        return solve(0,amount)     


        