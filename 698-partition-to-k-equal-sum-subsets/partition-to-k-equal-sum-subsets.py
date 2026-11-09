class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        sums=sum(nums)
        target=sums//k
        nums.sort(reverse=True)

        buckets=[0]*k
        n=len(nums)

        memo={}
        def solve(i):
            if i>=n:
                return True
            key = (i, tuple(buckets))
            if key in memo:
                return memo[key]

            for j in range(k):
                if buckets[j]+nums[i]<=target:
                    buckets[j]+=nums[i]

                    if solve(i+1):
                        memo[key]=True
                        return True
                    
                    buckets[j]-=nums[i]
            memo[key]=False
            return False
        return solve(0)
