class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        n=len(nums)
        maxArr=[0]*n
        prefix=[0]*n
        maxArr[0]=nums[0]
        maxm=nums[0]

        for i in range(1,n):
            if nums[i]>maxm:
                maxArr[i]=nums[i]
                maxm=nums[i]
            else:
                maxArr[i]=maxm
        for i in range(n):
            prefix[i]=math.gcd(nums[i],maxArr[i])

        prefix.sort()
        ans=0
        i=0
        j=n-1

        while i!=j and i<j:
            ans+=math.gcd(prefix[i],prefix[j])
            i+=1
            j-=1
        return ans

        
        
        


        