class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        n=len(intervals)
        end=intervals[0][1]
        print(intervals)
        for i in range(1,n):
            s=intervals[i][0]
            e=intervals[i][1]
            if s>=end:
                end=e
            else:
                count+=1
        return count
        