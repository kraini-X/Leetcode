class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans=[]
        missing=[]
        numSet=set(nums)
        for num in range(lower,upper+1):
            if num not in numSet:
                missing.append(num)
        if not missing:
            return []
        start=missing[0]
        n=len(missing)
        for i in range(1,n):
            if missing[i]==missing[i-1]+1:
                continue
            else:
                ans.append([start,missing[i-1]])
                start=missing[i]
        ans.append([start, missing[-1]])
        return ans


        

