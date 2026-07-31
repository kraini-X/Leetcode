class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n=len(costs)//2
        Acost = [cost[0] for cost in costs]
        Bcost = [cost[1] for cost in costs]
        memo={}
        def solve(idx,rem):
            if rem < 0:
                return float('inf')
            
            if idx==len(Acost):
                if rem==0:
                    return 0
                return float('inf')

            if (idx,rem) in memo:
                return memo[(idx,rem)]
            
            sendA=Acost[idx]+solve(idx+1,rem-1)
            sendB=Bcost[idx]+solve(idx+1,rem)
            memo[(idx,rem)]= min(sendA,sendB)
            
            return min(sendA,sendB)

        return solve(0,n)
        