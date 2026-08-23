class Solution:
    def findSum(self,num):
        sums=0
        while num>0:
            r=num%10
            sums+=r
            num=num//10
        return sums
    
    def findProd(self,num):
        prod=1
        while num>0:
            r=num%10
            prod*=r
            num=num//10
        return prod
    
    def checkDivisibility(self, n: int) -> bool:
        return True if n% (self.findSum(n)+self.findProd(n))==0 else False
        