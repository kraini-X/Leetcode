class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n=len(citations)
        if n==1:
            if citations[0]>=1:
                return 1
            else:
                return 0
        i=0
        print(citations)
        while i+1<n+1 and i+1<=citations[i]:
            i+=1
        return i