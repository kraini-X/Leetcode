class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        n=len(nums)
        l=0
        size=0

        for r in range(n):
            count[nums[r]]+=1

            while count[nums[r]]>k:
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    del count[nums[l]]
                
                l+=1
            
            size=max(size,r-l+1)
        return size

