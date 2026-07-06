class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        n=len(nums)
        diff=[0]*n
        mp=defaultdict(int)
        for i in range(n):
            diff[i]=nums[i]-i
        
        count=0
        
        mp[diff[0]]=1
        for j in range(1,n):
            soFar=j
            badPairs=soFar-mp[diff[j]]
            mp[diff[j]]+=1
            count+=badPairs
        return count

        
