class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)

        diff=[0]*n

        for l,r,v in shifts:
            if v==0:
                x=-1
            else:
                x=1
            
            diff[l]+=x
            if r+1<n:
                diff[r+1]-=x
        prefix=[0]*n
        curr=0
        for i in range(n):
            curr+=diff[i]
            prefix[i]=curr

        ans = [ord(ch) - ord('a') for ch in s]
        st=""
        for i in range(n):
            temp=(ans[i]+prefix[i])%26 # handles negative automatically
            st += chr(ord('a')+temp)
        return st