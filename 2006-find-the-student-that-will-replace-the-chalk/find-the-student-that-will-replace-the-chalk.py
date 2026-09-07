class Solution:
    def chalkReplacer(self, chalks: List[int], k: int) -> int:
        last=0
        n=len(chalks)
        k %= sum(chalks)
        i=0
        while k!=0:
            if chalks[i]>k:
                return i
            k-=chalks[i]
            i=(i+1)%n
        return i


        