class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        i=0
        j=1
        for k in range(n):
            if nums[k]>0:
                res[i]=nums[k]
                i+=2
            else:
                res[j]=nums[k]
                j+=2
        return res
        
        
        