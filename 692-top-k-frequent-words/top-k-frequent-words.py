class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq
        freq=Counter(words)
        heap=[]

        heap = [(-f, word) for word, f in freq.items()]
        heapq.heapify(heap)
        ans=[]
        for _ in range(k):
            freq,word=heapq.heappop(heap)
            ans.append(word)
        return ans

