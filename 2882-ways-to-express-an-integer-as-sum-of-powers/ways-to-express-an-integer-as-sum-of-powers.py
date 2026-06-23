class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        memo={}
        def solve(num,rem):
            if rem==0:
                return 1
            
            if rem<0:
                return 0

            if num**x > rem:
                return 0
            
            if (num,rem) in memo:
                return memo[(num,rem)]

            notTake=solve(num+1,rem)
            take=0
            if num<=rem:
                take=solve(num+1,rem-num**x)
            memo[(num,rem)]=take+notTake
            return take+notTake
        return solve(1,n)%(10**9+7)