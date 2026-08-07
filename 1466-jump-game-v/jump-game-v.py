class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n=len(arr)
        memo={}
        def dfs(i):
            if (i) in memo:
                return memo[(i)]
            left=1
            right=1

            #left
            for steps in range(1,d+1):
                j=i-steps

                if j<0:
                    break
                
                if arr[i]<=arr[j]:
                    break
                
                left=max(left,1+dfs(j))
            
            #right

            for steps in range(1,d+1):
                j=i+steps

                if j>=n:
                    break

                if arr[i]<=arr[j]:
                    break
                
                right=max(right,1+dfs(j))
            memo[(i)]=max(left,right)
            return max(left,right)
        
        ans=float('-inf')

        for i in range(n):
            ans=max(ans,dfs(i))
        return ans