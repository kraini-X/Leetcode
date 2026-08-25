class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=len(nums)
        minm=float('inf')
        for i in range(1,102):
            val=k*i
            if val<minm and val not in nums:
                minm=val
                break
        return minm
        