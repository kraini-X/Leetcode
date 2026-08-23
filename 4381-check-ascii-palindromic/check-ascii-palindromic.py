class Solution:
    def check(self,n):
        st=str(n)
        if n==n[::-1]:
            return True
        return False

    def isPalindromic(self, s: str) -> bool:
        st=""

        for ch in s:
            st+=str(bin(ord(ch))[2:])
        print(st)
        return self.check("0"+st)
        