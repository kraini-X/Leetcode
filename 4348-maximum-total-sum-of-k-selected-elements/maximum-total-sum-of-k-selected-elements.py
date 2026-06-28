class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        i=0
        ans=0
        while k!=0:
            if mul>0:
                ans+=nums[i]*mul
                i+=1
                mul-=1
                k-=1
            else:
                ans+=nums[i]
                i+=1
                mul-=1
                k-=1
        return ans


        