class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)
        isInc=False
        isDec=False
        first=nums[0]
        last=nums[-1]  

        if first<last:
            isInc=True
        else:
            isDec=True
        
        ans=False
        if isInc:
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    return False

        if isDec:
            for i in range(1, n):
                if nums[i - 1] < nums[i]:
                    return False
        return True
