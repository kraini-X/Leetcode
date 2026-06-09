class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minm=min(nums)
        maxm=max(nums)

        diff=maxm-minm
        return diff*k
        