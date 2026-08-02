class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n=len(s)
        prefix1=[0]*(n)
        prefix0=[0]*(n)

        if s[0]=="1":
            prefix1[0]=1
        else:
            prefix0[0]=1

        for i in range(1,n):
            if s[i]=="1":
                prefix1[i]=prefix1[i-1]+1
                prefix0[i]=prefix0[i-1]
            else:
                prefix0[i]=prefix0[i-1]+1
                prefix1[i]=prefix1[i-1]
        
        count=0

        for i in range(n):
            count0=prefix0[i]
            count1=prefix1[i]

            if abs(count0-count1) in [0,1]:
                count+=1
        return count