class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        mp=defaultdict(int)
        mp[0]=1
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        count=0
        for i in range(n):
            count+=mp[prefix[i] - k]
            mp[prefix[i]]+=1
        return count
        

        