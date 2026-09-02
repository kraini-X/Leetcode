class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        res=[]
        def solve(i,exp,val,prev):
            if i>=n:
                if val==target:
                    res.append(exp)
                return
            

            for j in range(i,n):
                if j>i and num[i]=="0":
                    break
                
                curr=int(num[i:j+1])
                if i==0:
                    solve(j+1,exp+str(curr),curr,curr)
                else:
                    solve(
                        j+1,
                        exp+"+"+str(curr),
                        val+curr,
                        curr

                    )
                    solve(
                        j+1,
                        exp+"-"+str(curr),
                        val-curr,
                        -curr

                    )

                    solve(
                        j+1,
                        exp+"*"+str(curr),
                        val - prev + prev * curr,
                        prev * curr

                    )
        solve(0,"",0,0)
        return res
                
                
                


