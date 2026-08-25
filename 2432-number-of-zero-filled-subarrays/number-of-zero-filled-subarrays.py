class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)

        i=0
        while i<n:
            if nums[i]==0:
                m=0
                j=i

                while j<n and nums[j]==0:
                    m+=1
                    j+=1
                i=j+1
                ans+=m*(m+1)//2
            else:
                i+=1
        return ans
        

        