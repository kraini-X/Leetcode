class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        num=0
        for i in range(len(digits)):
            num+=digits[i]*10**(n-1-i)
        inc=num+1
        res=[]
        while inc>0:
            r=inc%10
            res.append(r)
            inc=inc//10
        return res[::-1]
