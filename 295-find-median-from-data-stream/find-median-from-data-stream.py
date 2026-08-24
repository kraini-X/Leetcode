class MedianFinder:
    import heapq

    def __init__(self):
        self.leftMax=[]
        self.rightMin=[]
        

    def addNum(self, num: int) -> None:
        if not self.leftMax or num<-self.leftMax[0]:
            heapq.heappush(self.leftMax,-num)
        
        else:
            heapq.heappush(self.rightMin,num)
        
        if len(self.rightMin)>len(self.leftMax):
            val=heapq.heappop(self.rightMin)
            heapq.heappush(self.leftMax,-val)

        elif len(self.leftMax) > len(self.rightMin) + 1:
            val = -heapq.heappop(self.leftMax)
            heapq.heappush(self.rightMin, val)
        

    def findMedian(self) -> float:
        if len(self.leftMax)==len(self.rightMin)+1:
            return -self.leftMax[0]
        
        return (-self.leftMax[0]+self.rightMin[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()