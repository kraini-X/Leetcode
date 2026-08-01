class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)

        memo={}
        def solve(i,j):
            if i==j:
                return nums[i]
            if (i,j) in memo:
                return memo[(i,j)]
            takeFirst=nums[i]-solve(i+1,j)
            takeLast=nums[j]-solve(i,j-1)
            memo[(i,j)]=max(takeFirst,takeLast)
            return max(takeFirst,takeLast)
        
        return solve(0,n-1)>=0
        