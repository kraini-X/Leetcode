class Solution:
    def filterOccupiedIntervals(self, intervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:

        intervals.sort()
        merged=[intervals[0]]
        n=len(intervals)

        for i in range(1,n):
            start=intervals[i][0]
            end=intervals[i][1]

            if merged[-1][1]>=start:
                merged[-1]=[merged[-1][0],max(end,merged[-1][1])]
            elif merged[-1][1]+1==start:
                merged[-1]=[merged[-1][0],max(end,merged[-1][1])]
            else:
                merged.append([start,end])
        ans=[]
        for l,r in merged:
            if l <= freeEnd and r >= freeStart:
                if l<freeStart:
                    ans.append([l,freeStart-1])
                
                if r>freeEnd:
                    ans.append([freeEnd+1,r])
            
            else:
                ans.append([l,r])
                
        return ans

