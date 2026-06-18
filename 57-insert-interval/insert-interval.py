class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            start=intervals[i][0]
            end=intervals[i][1]

            if merged[-1][1]>=start:
                merged[-1]=[merged[-1][0],max(merged[-1][1],end)]
            else:
                merged.append([start,end])
        return merged
        

        