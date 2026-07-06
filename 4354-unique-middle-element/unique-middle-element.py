class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        if nums.count(nums[n//2])==1:
            return True
        return False
        