class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        import heapq
        pq=[]

        for pro,diff in zip(profit,difficulty):
            heapq.heappush(pq,(-pro,diff))
        
        worker.sort(reverse=True)

        i=0
        m=len(worker)
        ans=0
        while i<m and pq:
            pro,diff=pq[0]

            if diff>worker[i]:
                heapq.heappop(pq)
            
            else:
                ans+=-pro
                i+=1
        return ans
        