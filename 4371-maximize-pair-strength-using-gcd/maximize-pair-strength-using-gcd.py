class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        import math
        ans=float('-inf')

        n=len(nums)

        for i in range(n):
            for j in range(n):
                if i!=j:
                    val=nums[i]*nums[j]
                    ans=max(ans,val//(math.gcd(nums[i],nums[j])**2))
        return ans
        