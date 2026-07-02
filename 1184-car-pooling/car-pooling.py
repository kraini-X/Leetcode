class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cars=[]
        for seats,start,end in trips:
            cars.append([start,seats])
            cars.append([end,-seats])
        
        cars.sort(key=lambda x:(x[0],x[1]))

        curr=0
        maxm=0
        for start,seats in cars:
            curr+=seats
            if curr>capacity:
                return False
            if curr>maxm:
                maxm=curr
        return True