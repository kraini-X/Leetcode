class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=min(nums)
        r=max(nums)
        ans=[]

        for num in range(l,r+1):
            if num not in nums:
                ans.append(num)
        return ans