class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        pq=[]
        for st in stones:
            heapq.heappush(pq,-st)
        
        while len(pq)>1:
            first=-heapq.heappop(pq)
            second=-heapq.heappop(pq)
            diff=first-second
            heapq.heappush(pq,-diff)
        return -pq[0] if pq else 0

        