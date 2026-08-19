class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n=len(fruits)
        diagonal_sum=0
        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += fruits[i][i]

        memo2={}
        memo3={}   

        def child2(i,j):
            if i<0 or i>=n or j<0 or j>=n:
                return float('-inf')
            if i==j:
                return 0
            if i==n-1 and j==n-1:
                return fruits[n-1][n-1]
            
            if (i,j) in memo2:
                return memo2[(i,j)]

            ans=fruits[i][j]+max(
                child2(i+1,j-1),
                child2(i+1,j),
                child2(i+1,j+1)
            )
            memo2[(i,j)]=ans
            return ans
        
        def child3(i,j):
            if i<0 or i>=n or j<0 or j>=n:
                return float('-inf')
            if i==j:
                return 0
            if i==n-1 and j==n-1:
                return fruits[n-1][n-1]
            if (i,j) in memo3:
                return memo3[(i,j)]
            ans=fruits[i][j]+max(
                child3(i-1,j+1),
                child3(i,j+1),
                child3(i+1,j+1)
            )
            memo3[(i,j)]=ans
            return ans
        
        return diagonal_sum+child2(0,n-1)+child3(n-1,0)

        