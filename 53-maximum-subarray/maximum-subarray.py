class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=nums[0]
        maxSum=nums[0]

        n=len(nums)
        for i in range(1,n):
            currSum=max(nums[i],currSum+nums[i])
            maxSum=max(currSum,maxSum)
        return maxSum
        