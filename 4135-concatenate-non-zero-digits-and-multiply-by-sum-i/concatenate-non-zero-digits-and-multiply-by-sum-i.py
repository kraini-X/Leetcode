class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sums=0
        num=[]
        while n>0:
            r=n%10
            if r>0:
                num.append(r)
                sums+=r
            n=n//10
        num=num[::-1]
        new=0
        if num:
            new=int("".join(str(x) for x in num))
        return new*sums
        
        
        