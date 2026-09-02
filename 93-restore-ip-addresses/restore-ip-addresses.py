class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n=len(s)
        res=[]
        def solve(idx,temp):
            if idx>=n and len(temp)==4:

                res.append(".".join(temp))
                return
            
            for i in range(3):
                if idx+i>=n:
                    break
                new_idx=idx+i
                part=s[idx:new_idx+1]

                if len(part)>1 and part[0]=="0":
                    continue
                
                if 0<=int(part)<=255:
                    temp.append(part)
                    solve(new_idx+1,temp)
                    temp.pop()
        solve(0,[])
        return res
                

