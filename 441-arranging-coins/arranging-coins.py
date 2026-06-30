class Solution:
    def arrangeCoins(self, n: int) -> int:

        def coins_needed(row):
            return row*(row+1)//2
        
        left=1
        right=n

        while left<=right:
            mid=(left+right)//2

            if coins_needed(mid)>n:
                right=mid-1
            else:
                left=mid+1
        return left-1

        