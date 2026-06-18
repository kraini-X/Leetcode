class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        n=len(nums)
        i=0
        while i<n:
            start=nums[i]
            j=i
            while j+1<n and nums[j+1]-nums[j]==1:
                j+=1
            if j-i>0:
                ans.append(f"{start}->{nums[j]}")
            else:
                ans.append(str(start))
            i=j+1
        return ans