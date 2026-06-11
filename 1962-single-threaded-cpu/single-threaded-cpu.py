class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        arr = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        arr.sort()
        pq=[]
        res=[]
        currTime=1
        i=0
        n=len(tasks)

        while i<n or pq:
            if not pq and currTime<arr[i][0]:
                currTime=arr[i][0]
            
            while i<n and arr[i][0]<=currTime:
                at,bt,idx=arr[i]
                heapq.heappush(pq,(bt,idx))
                i+=1
            bt,idx=heapq.heappop(pq)
            currTime+=bt
            res.append(idx)
        return res
            