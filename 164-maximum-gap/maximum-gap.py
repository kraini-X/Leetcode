class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n<2:
            return 0
        ans=float('-inf')
        for i in range(n-1):
            ans=max(ans,nums[i+1]-nums[i])
        return ans

        