class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        size=float('inf')

        sums=0

        for r in range(l,n):
            sums+=nums[r]

            while sums>=target:
                size=min(size,r-l+1)
                sums-=nums[l]
                l+=1  
                
        return size if size!=float('inf') else 0
            

        