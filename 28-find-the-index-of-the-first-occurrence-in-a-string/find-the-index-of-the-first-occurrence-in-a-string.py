class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def build_lps(pattern):
            n=len(pattern)
            lps=[0]*n

            length=0
            i=1

            while i<n:
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

        lps=build_lps(needle)
        n=len(haystack)
        m=len(needle)
        i=0
        j=0

        while i<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1

                if j==m:
                    return i-j

            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1


        