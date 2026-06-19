class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        used=[False]*n
        res=[]
        def solve(temp):

            if len(temp)==n:
                res.append(temp[:])
            
            for i in range(n):
                if not used[i]:
                    temp.append(nums[i])
                    used[i]=True
                    solve(temp)
                    temp.pop()
                    used[i]=False
        solve([])
        return res
