class Solution:
    def trap(self, heights: List[int]) -> int:
        n=len(heights)

        prefixMax=[0]*n
        suffixMax=[0]*n

        prefixMax[0]=heights[0]
        suffixMax[n-1]=heights[n-1]

        for i in range(1,n):
            prefixMax[i]=max(prefixMax[i-1],heights[i])
        
        for i in range(n-2,-1,-1):
            suffixMax[i]=max(suffixMax[i+1],heights[i])
        total=0
        for i in range(n):
            total+=min(prefixMax[i],suffixMax[i])-heights[i]
        return total
            