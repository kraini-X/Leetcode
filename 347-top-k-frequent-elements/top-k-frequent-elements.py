class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        freq=Counter(nums)
        pq=[]
        
        for num,freq in freq.items():
            heapq.heappush(pq,(freq,num))
        
        while len(pq)>k:
            heapq.heappop(pq)
        ans=[]
        while pq:
            freq,num=heapq.heappop(pq)
            ans.append(num)
        return ans
        