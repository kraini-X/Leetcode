class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n=len(monsters)
        diff=[0]*(n+1)

        for l,r,v in boosts:
            diff[l]+=v
            if r+1<n:
                diff[r+1]-=v
        
        bonus = [0] * n

        curr = 0
        for i in range(n):
            curr += diff[i]
            bonus[i] = curr
        
        def check(strength,bonus):
            defeated=[False]*n
            for i in range(n):
                if strength+bonus[i]>=monsters[i]:
                    strength=max(0,strength-monsters[i])
                    defeated[i]=True
            return True if all(i==True for i in defeated) else False
        
        low=0
        high=sum(monsters)
        #print(high)
        while low<=high:
            mid=(low+high)//2

            if check(mid,bonus):
                high=mid-1
            else:
                low=mid+1
        return low