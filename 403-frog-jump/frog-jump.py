class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n=len(stones)
        stones_set=set(stones)
        memo = {}
        def solve(pos,jumps):
            if pos==stones[-1]:
                return True
            if (pos,jumps) in memo:
                return memo[(pos,jumps)]
            for k in [jumps-1,jumps,jumps+1]:
                if k>0 and pos+k in stones_set:
                    if solve(pos+k,k):
                        memo[(pos,jumps)]=True
                        return True
            memo[(pos,jumps)]=False
            return False
        return solve(0,0)            
             