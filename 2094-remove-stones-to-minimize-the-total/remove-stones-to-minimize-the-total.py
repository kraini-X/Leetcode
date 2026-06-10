class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        pq=[]
        ans=0
        for p in piles:
            heapq.heappush(pq,-p)

        while k>0:
            num=-heapq.heappop(pq)
            new=num-(num//2)
            heapq.heappush(pq,-new)
            k-=1

        sums=0
        for num in pq:
            sums+=-num
        return sums
        