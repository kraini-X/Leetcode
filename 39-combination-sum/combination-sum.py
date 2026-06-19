class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        def solve(idx,target,temp):

            if target==0:
                res.append(temp[:])
                return
            
            for j in range(idx,n):
                if nums[j]<=target:
                    temp.append(nums[j])
                    solve(j,target-nums[j],temp)
                    temp.pop()
        solve(0,target,[])
        return res


            

        