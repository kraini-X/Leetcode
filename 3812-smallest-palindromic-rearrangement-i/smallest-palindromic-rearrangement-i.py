class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        n=len(s)
        res=[""]*n
        freq=Counter(s)
        sorted_freq=dict(sorted(freq.items()))

        i=0

        for key,val in sorted_freq.items():
            while val>=2:
                res[i]=key
                res[n-1-i]=key

                val-=2
                sorted_freq[key]-=2
                i+=1
        for key in sorted_freq:
            if sorted_freq[key] == 1:
                res[n // 2] = key
                break

        return "".join(res)