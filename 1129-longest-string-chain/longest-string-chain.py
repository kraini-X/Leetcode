class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)

        def isPred(shorter, longer):
            if len(longer) != len(shorter) + 1:
                return False

            i = j = 0

            while i < len(shorter) and j < len(longer):
                if shorter[i] == longer[j]:
                    i += 1
                j += 1

            return i == len(shorter)
        
        dp=[[-1]*(n+1) for _ in range(n+1)]
        def solve(idx,pred):
            if idx==n:
                return 0
            
            if dp[idx][pred]!=-1:
                return dp[idx][pred]
            word=words[idx]
            take=0
            if pred==-1 or isPred(words[pred],word):
                take=1+solve(idx+1,idx)
            
            skip=solve(idx+1,pred)
            dp[idx][pred]=max(take,skip)
            return max(take,skip)
        return solve(0,-1)