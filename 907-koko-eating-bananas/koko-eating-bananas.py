class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def speed(arr,rt):
            total=0
            for num in arr:
                total+=math.ceil(num/rt)
            return total
        #print(speed(piles,4))
        
        low=1
        high=max(piles)

        while low<=high:
            mid=(low+high)//2

            if speed(piles,mid)>h:
                low=mid+1
            else:
                high=mid-1
        return low


    
        