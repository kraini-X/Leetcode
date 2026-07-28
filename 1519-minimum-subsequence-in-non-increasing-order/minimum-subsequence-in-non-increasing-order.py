class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        suffix=[0]*n
        suffix[n-1]=nums[n-1]
        total=sum(nums)
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i]+suffix[i+1]
        
        temp=0
        for i in range(n-1,-1,-1):
            if suffix[i]>total-suffix[i]:
                temp=i
                break
            
        return sorted(nums[i:],reverse=True)

        


        