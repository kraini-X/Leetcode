class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def build_lps(pattern):
            n=len(s)
            lps=[0]*(2*n+1)
            i=1
            length=0

            while i<(2*n)+1:
                if pattern[i]==pattern[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                
                else:
                    if length!=0:
                        length=lps[length-1]
                    
                    else:
                        lps[i]=0
                        i+=1
            return lps
        pattern=s+"#"+s[::-1]
        lps=build_lps(pattern)
        longest=lps[-1]

        return s[longest:][::-1] + s
        