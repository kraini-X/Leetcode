class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalGap=[0]*(len(horizontalCuts)+1)
        verticalGap=[0]*(len(verticalCuts)+1)

        horizontalGap[0]=horizontalCuts[0]
        horizontalGap[-1]=h-horizontalCuts[-1]

        verticalGap[0]=verticalCuts[0]
        verticalGap[-1]=w-verticalCuts[-1]

        for i in range(1,len(horizontalCuts)):
            horizontalGap[i]=horizontalCuts[i]-horizontalCuts[i-1]
        
        for i in range(1,len(verticalCuts)):
            verticalGap[i]=verticalCuts[i]-verticalCuts[i-1]

        mod=10**9+7
        print(horizontalGap)
        print(verticalGap)
        return max(verticalGap)*max(horizontalGap)%mod