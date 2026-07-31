class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], L: int, M: int) -> int:
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        def solve(nums, L, M):
            n=len(nums)
            ans=0
            for Lstart in range(n-L+1):
                Lend=Lstart+L-1
                Lsum=prefix[Lend+1]-prefix[Lstart]

                for Mstart in range(n-M+1):
                    Mend=Mstart+M-1

                    if Mstart>Lend or Mend<Lstart:
                        Msum=prefix[Mend+1]-prefix[Mstart]

                        ans=max(ans,Msum+Lsum)
            return ans
            
        return max(
            solve(nums,L,M),
            solve(nums,M,L)
        )



