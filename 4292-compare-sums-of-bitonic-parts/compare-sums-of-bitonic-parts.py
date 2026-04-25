class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        maxm=max(nums)
        n=len(nums)
        peak=0
        for i in range(n):
            if nums[i]==maxm:
                peak=i
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=nums[0]
        suffix[n-1]=nums[n-1]

        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]+nums[i]

        asc=prefix[peak]
        desc=suffix[peak]

        if asc>desc:
            return 0
        elif asc<desc:
            return 1
        else:
            return -1
        