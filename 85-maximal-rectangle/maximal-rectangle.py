class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        pse = [-1] * n
        nse = [n] * n


        stack=[]
        #nse
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        
        #pse
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            stack.append(i)
        ans=0
        for i in range(n):
            width=nse[i]-pse[i]-1
            ans=max(ans,heights[i]*width)
        return ans
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        heights = [0] *n
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    heights[j]+=1
                else:
                    heights[j]=0
            ans=max(ans,self.largestRectangleArea(heights))
        return ans
            

        