class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq
        freq=Counter(s)
        n=len(s)
        pq=[]
        ans=""
        for key,val in freq.items():
            if val>(n+1)//2:
                return ""
            heapq.heappush(pq,(-val,key))
        
        while len(pq)>=2:
            count1, char1 = heapq.heappop(pq)
            count1 = -count1
        
            count2, char2 = heapq.heappop(pq)
            count2 = -count2

            ans+=char1
            ans+=char2
            count1-=1
            count2-=1

            if count1>0:
                heapq.heappush(pq,(-count1,char1))
            
            if count2>0:
                heapq.heappush(pq,(-count2,char2))
        
        if pq:
            ans+=pq[0][1]
        return ans
            



        