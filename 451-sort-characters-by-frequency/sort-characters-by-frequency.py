class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        from collections import Counter
        freq=Counter(s)
        
        pq=[]
        ans=[]
        
        for ch, cnt in freq.items():
            heapq.heappush(pq, (-cnt, ch))
        
        while pq:
            freq,ch=heapq.heappop(pq)
            ans.append(ch*(-freq))
        return "".join(ans)
