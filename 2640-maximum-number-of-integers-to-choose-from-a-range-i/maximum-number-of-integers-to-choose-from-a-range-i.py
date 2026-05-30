class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count=0
        bannd=set(banned)
        for i in range(1,n+1):
            if i not in bannd and i<=maxSum:
                maxSum-=i
                count+=1
        return count

        