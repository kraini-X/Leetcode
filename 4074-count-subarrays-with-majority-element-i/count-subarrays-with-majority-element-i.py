class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count=0
        n=len(nums)
        for l in range(n):
            freq=0
            for r in range(l,n):
                if nums[r]==target:
                    freq+=1

                length=r-l+1
                if freq>length//2:
                    count+=1
        return count
        