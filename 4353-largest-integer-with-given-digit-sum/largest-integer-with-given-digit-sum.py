class Solution:
    def largestInteger(self, n: int, s: int) -> int:

        if s > 9 * n:
            return -1
        res=0
        temp=n-1
        for i in range(n):
            digit=min(9,s)
            res+=10**(temp)*digit
            temp-=1
            s-=digit
        return res
        
            
        