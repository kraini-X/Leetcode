class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        mod=10**9 + 7
        dp=[[-1]*(10) for _ in range(n+1)]
        def solve(n,digit):
            if n==0:
                return 1
            if dp[n][digit]!=-1:
                return dp[n][digit]
            res=0
            for cell in adj[digit]:
                res+=solve(n-1,cell)
            dp[n][digit]=res%mod
            return res%mod

        count=0
        for i in range(0,10):
            count+=solve(n-1,i)
        return count%mod
        

        