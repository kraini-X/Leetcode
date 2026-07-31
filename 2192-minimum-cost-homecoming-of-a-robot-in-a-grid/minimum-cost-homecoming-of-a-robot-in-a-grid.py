class Solution:
    import heapq
    def minCost(self, startPos: List[int], homePos: List[int], rowCost: List[int], colCost: List[int]) -> int:
        m=len(rowCost)
        n=len(colCost)
        
        sr,sc=startPos
        hr,hc=homePos
        cost=0
        if sr<hr:
            for r in range(sr+1,hr+1):
                cost+=rowCost[r]
        else:
            for r in range(sr-1,hr-1,-1):
                cost+=rowCost[r]
            
        if sc < hc:
            for c in range(sc + 1, hc + 1):
                cost += colCost[c]
        else:
            for c in range(sc - 1, hc - 1, -1):
                cost += colCost[c]
        return cost