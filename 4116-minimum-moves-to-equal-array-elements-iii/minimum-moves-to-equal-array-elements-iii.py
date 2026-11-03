class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxm=max(nums)
        ans=0

        for num in nums:
            ans+=abs(maxm-num)
        return ans
        