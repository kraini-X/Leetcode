class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n=len(pairs)
        pairs.sort()

        memo={}
        def solve(idx,prevMax):
            if idx==n:
                return 0
            
            if (idx,prevMax) in memo:
                return memo[(idx,prevMax)]
            skip=solve(idx+1,prevMax)

            take=0

            curr=pairs[idx][0]

            if curr>prevMax:
                take=1+solve(idx+1,pairs[idx][1])

            memo[(idx,prevMax)]=max(take,skip)
            return max(take,skip)
        return solve(0,float('-inf'))
        