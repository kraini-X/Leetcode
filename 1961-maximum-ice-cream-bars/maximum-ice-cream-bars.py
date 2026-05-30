class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        n=len(costs)
        for i in range(n):
            if costs[i]<=coins:
                coins-=costs[i]
                count+=1
        return count
        