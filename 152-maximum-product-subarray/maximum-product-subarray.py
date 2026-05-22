class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax=nums[0]
        currMin=nums[0]
        ans=nums[0]
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(1,n):
            temp=currMax
            currMax=max(nums[i],currMax*nums[i],currMin*nums[i])
            currMin=min(nums[i],temp*nums[i],currMin*nums[i])
            ans=max(ans,currMax)
        return ans
        