class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n=len(heights)
        ans=[0]*n
        stack=[]

        for i in range(n-1,-1,-1):
            while stack and heights[i]>stack[-1]:
                ans[i]+=1
                stack.pop()
            
            if stack:
                ans[i]+=1
            
            stack.append(heights[i])

        return ans