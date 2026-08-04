class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def check(nums,queries,mid):
            n=len(nums)
            diff=[0]*len(nums)
            for i in range(mid):
                l=queries[i][0]
                r=queries[i][1]
                val=queries[i][2]

                diff[l]+=val
                if r+1<n:
                    diff[r+1]-=val
                
            currSum=0
            budget=[0]*n
            for i in range(n):
                currSum+=diff[i]
                    
                budget[i]=currSum
            return True if all(budget[i]>=nums[i] for i in range(n)) else False
        
        left=0
        right=len(queries)

        while left<right:
            mid=(left+right)//2

            if check(nums,queries,mid):
                right=mid
            
            else:
                left=mid+1

        if not check(nums, queries, left):
            return -1

        return left
        

