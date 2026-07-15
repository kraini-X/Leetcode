class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        area=0
        while left<right:
            minVal=min(height[left],height[right])
            area=max(area,minVal*(right-left))

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area
