class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        def solve(idx,opn):
            if opn<0:
                return False
            if idx>=n:
                if opn==0:
                    return True
                return False
                
            if dp[idx][opn]!=-1:
                return dp[idx][opn]
                
            if s[idx]=="(":
                val=solve(idx+1,opn+1)
                dp[idx][opn]=val
                return val
            if s[idx]==")":
                val=solve(idx+1,opn-1)
                dp[idx][opn]=val
                return val
            valid=False
            if s[idx]=="*":
                valid=solve(idx+1,opn+1) or solve(idx+1,opn-1) or solve(idx+1,opn)
            dp[idx][opn]=valid
            return valid
        return solve(0,0)

            

        