class Solution:
    def maxProduct(self, n: int) -> int:
        ans=0
        temp=[]
        while n>0:
            r=n%10
            temp.append(r)
            n=n//10
        temp.sort()

        return temp[-1]*temp[-2]
