class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        res=[]
        def solve(idx,target,temp):
            if target==0:
                res.append(temp[:])
                return
            
            for i in range(idx,n):
                if i >idx and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i]>target:
                    break
                
                temp.append(candidates[i])
                solve(i+1,target-candidates[i],temp)
                temp.pop()
        solve(0,target,[])
        return res


        