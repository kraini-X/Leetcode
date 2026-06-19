class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)

        def isValid(s):
            if s==s[::-1]:
                return True
            return False
        temp=[]
        res=[]
        def solve(idx,temp):
            if idx==n:
                res.append(temp.copy())
                return
            
            for j in range(idx,n):
                if isValid(s[idx:j+1]):
                    temp.append(s[idx:j+1])
                    solve(j+1,temp)
                    temp.pop()
        solve(0,temp)
        return res

        