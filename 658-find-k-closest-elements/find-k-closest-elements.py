class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq

        pq=[]
        ans=[]
        for num in arr:
            diff=abs(num-x)
            heapq.heappush(pq,(-diff,-num))

            if len(pq)>k:
                heapq.heappop(pq)
        
        while len(pq)>0:
            diff,num=heapq.heappop(pq)
            ans.append(-num)
        return sorted(ans)
        