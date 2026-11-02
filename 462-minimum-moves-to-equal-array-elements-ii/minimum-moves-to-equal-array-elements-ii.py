class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        def findMoves(nums,target):
            ans=0
            for num in nums:
                ans+=abs(target-num)
            return ans
        
        n=len(nums)
        mid=n//2

        return findMoves(nums,nums[mid])
        
        

        