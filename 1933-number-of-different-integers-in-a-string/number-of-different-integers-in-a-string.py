class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        n=len(word)
        res=set()
        i=0
        while i<n:
            if word[i].isdigit():
                st=word[i]
                count=0
                for j in range(i+1,n):
                    if word[j].isdigit():
                        st+=word[j]
                        count+=1
                    else:
                        i=i+count
                        break
                else:
                    i+=count
                res.add(st.lstrip('0'))
            i+=1
        return len(res)
                

        