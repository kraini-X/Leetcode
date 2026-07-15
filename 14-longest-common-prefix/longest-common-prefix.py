class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def compare(s1,s2):
            i=0
            j=0
            count=0
            m=len(s1)
            n=len(s2)

            while i<m and j<n and s1[i]==s2[j]:
                i+=1
                j+=1
                count+=1
            return count
        ref=strs[0]
        maxCount=100
        for i in range(1,len(strs)):
            maxCount=min(maxCount,compare(ref,strs[i]))
        
        return ref[0:maxCount]


                

        