class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n=len(locations)
        memo={}
        mod=10**9+7
        def solve(start,dest,fuel):
            if fuel<0:
                return 0
            count=0
            if start==dest:
                if fuel<=0:
                    return 1
                else:
                    count=1
            if (start,dest,fuel) in memo:
                return memo[(start,dest,fuel)]
                           
            for j in range(n):
                if j!=start:
                    diff=abs(locations[start]-locations[j])
                    count+=solve(j,dest,fuel-diff)
            memo[(start,dest,fuel)]=count
            return count
        return solve(start,finish,fuel)%mod

        