class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def solve(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            
            if (i,j) in memo:
                return memo[(i,j)]
            ans=0
            ans+=solve(i+1,j)
            ans+=solve(i,j+1)


            memo[(i,j)]=ans
            return ans
        return solve(0,0)