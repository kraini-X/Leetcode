class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        memo={}
        def solve(i,j):
            if i>j:
                return 0
            
            if i==j:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]
            ans=0

            if s[i]==s[j]:
                ans=2+solve(i+1,j-1)
            
            else:
                ans=max(
                    solve(i+1,j),
                    solve(i,j-1)
                )
            memo[(i,j)]=ans
            return ans
            
        return solve(0,n-1)
