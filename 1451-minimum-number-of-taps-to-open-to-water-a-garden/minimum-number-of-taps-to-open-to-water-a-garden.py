class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rng=[[0,0] for _ in range(n+1)]

        for i in range(n+1):
            rng[i][0]=max(0,i-ranges[i])
            rng[i][1]=min(n,i+ranges[i])

        maxStart=[0]*(n+1)
        currEnd=0
        maxEnd=0
        taps=0
        for u,v in rng:
            maxStart[u]=max(maxStart[u],v)
        print(rng)
        print(maxStart)
        for i in range(n+1):
            
            if i>maxEnd:
                return -1
            if i>currEnd:
                taps+=1
                currEnd=maxEnd
            maxEnd=max(maxEnd,maxStart[i])

            
        return taps

        


        

        