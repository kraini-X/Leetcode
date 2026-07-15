class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def solve(idx,temp):

            if len(temp)==k:
                res.append(temp[:])
                return
            

            for i in range(idx,n+1):
                temp.append(i)
                solve(i+1,temp)
                temp.pop()
        solve(1,[])
        return res
            



        