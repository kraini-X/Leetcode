class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*n

        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        
        i = 1

        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1

        temp=prefix[i-1]

        if temp not in nums:
            return temp
        else:
            while temp+1 in nums:
                temp+=1
            return temp+1