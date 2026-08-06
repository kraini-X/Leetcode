class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def check(n,t):
            prod=1
            while n>0:
                r=n%10
                prod*=r
                n=n//10
            
            return prod%t==0
        
        for i in range(n,100+1):
            if check(i,t):
                return i