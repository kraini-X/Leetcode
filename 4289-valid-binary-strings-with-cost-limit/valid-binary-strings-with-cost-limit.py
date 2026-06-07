class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res=[]
        def solve(temp):
            if len(temp)==n:
                res.append("".join(temp))
                return
            
            
            temp.append("0")
            solve(temp)
            temp.pop()
        
            temp.append("1")
            solve(temp)
            temp.pop()
        solve([])
        final=[]

        for bn in res:
            ans=0
            valid=True
            for i in range(n):
                if i+1<n and bn[i]=="1" and bn[i+1]=="1":
                    valid=False
                    break
                if bn[i]=="1":
                    ans+=i
            if valid and ans<=k:
                final.append(bn)
        return final






        