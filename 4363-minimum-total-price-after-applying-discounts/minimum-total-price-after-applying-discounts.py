class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts.sort(reverse=True)
        prices.sort(reverse=True)
        
        ans=0
        m=len(prices)
        n=len(discounts)
        for i in range(m):
            if i>=n:
                ans+=prices[i]
            else:
                p=prices[i]
                d=discounts[i]
                ans+=(p*(100-d))/100
        return ans