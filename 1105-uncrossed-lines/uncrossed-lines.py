class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)

        memo={}
        def solve(i,j):
            if i==m or j==n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if nums1[i]==nums2[j]:
                ans=1+solve(i+1,j+1)
                memo[(i,j)]=ans
                return ans
            else:
                ans=max(
                    solve(i+1,j),
                    solve(i,j+1)
                )
                memo[(i,j)]=ans
                return ans
        return solve(0,0)
        