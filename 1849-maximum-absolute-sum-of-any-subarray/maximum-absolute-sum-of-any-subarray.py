class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currSum=nums[0]
        maxSum=nums[0]
        minSum=nums[0]
        n=len(nums)

        for i in range(1,n):
            currSum=max(nums[i],currSum+nums[i])
            maxSum=max(maxSum,currSum)

        currSum=nums[0]
        
        for i in range(1,n):
            currSum=min(nums[i],currSum+nums[i])
            minSum=min(minSum,currSum)
        
        return max(abs(minSum),abs(maxSum))

        
        