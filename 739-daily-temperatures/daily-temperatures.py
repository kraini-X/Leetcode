class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack=[]
        
        n=len(arr)
        ans=[0]*n
        for i in range(n-1,-1,-1):

            while stack and arr[i]>=arr[stack[-1]]:
                stack.pop()
            
            if stack:
                ans[i]=abs(i-stack[-1])
            
            stack.append(i)
        return ans

        