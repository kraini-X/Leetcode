class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        rearranged=[]
        n=len(nums)
        for num in nums:
            digits=list(str(num))
            digits.sort(reverse=True)
            rearranged.append(max(num,int("".join(map(str, digits)))))
        
        pairs = list(zip(nums, rearranged))

        pairs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        ans=0
        
        for i in range(k):
            og=pairs[i][0]
            new=pairs[i][1]
            ans+=new
        for j in range(k,n):
            og=pairs[j][0]
            ans+=og
        return ans
        