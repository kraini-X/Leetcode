class Solution:
    def punishmentNumber(self, n: int) -> int:

        def solve(s,idx,target):
            if idx==len(s):
                return target==0
            
            for j in range(idx,len(s)):
                num=int(s[idx:j+1])
                if solve(s,j+1,target-num):
                    return True
            return False
            
        sums=0
        for i in range(1,n+1):
            if solve(str(i**2),0,i):
                sums+=i**2
        return sums
        