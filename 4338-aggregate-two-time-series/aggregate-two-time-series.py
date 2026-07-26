class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        m=len(series1)
        n=len(series2)
        i=0
        j=0
        res=[]
        while i<m or j<n:
            t1=series1[i][0] if i<m else float('inf')
            t2=series2[j][0] if j<n else float('inf')

            if t1<t2:
                t2val=0 if t2==float('inf') else series2[j][1]
                res.append([t1,series1[i][1]+t2val])
                i+=1
            elif t1>t2 and j<n:
                t1val=0 if t1==float('inf') else series1[i][1]
                res.append([t2,t1val+series2[j][1]])
                j+=1
            
            else:
                res.append([t2,series1[i][1]+series2[j][1]])
                i+=1
                j+=1
                
        return res





