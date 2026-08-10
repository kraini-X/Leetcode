class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        import math
        memo={}
        def solve(n):
            if n==0:
                return False
            if n in memo:
                return memo[(n)]
            for i in range(1, math.isqrt(n) + 1):
                square = i * i

                if not solve(n - square):
                    memo[(n)]=True
                    return True
            memo[(n)]=False
            return False
        return solve(n)
            


        