class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        import math
        intervals.sort(key=lambda x: x[0])

        merged = []

        for start,end in intervals:
            if not merged or start>merged[-1][1]:
                merged.append([start,end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

            
        length=0
        print(merged)
        for s,e in merged:
            length+=(e-s)+1

        bulbs=math.ceil(brightness/3)
        return bulbs*length
             