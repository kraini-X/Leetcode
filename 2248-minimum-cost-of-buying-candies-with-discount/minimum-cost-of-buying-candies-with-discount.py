class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n=len(cost)
        ans=0
        i=0
        j=1
        while i < n:
            ans += cost[i]          # first candy

            if i + 1 < n:
                ans += cost[i + 1]  # second candy

            # i+2 is the free candy (if it exists)

            i += 3
        return cost[0] if n==1 else ans

        