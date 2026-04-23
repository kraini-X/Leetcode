class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def diff(st1,st2):
            count=0
            n=len(st1)
            for i in range(n):
                if st1[i]!=st2[i]:
                    count+=1
            return count
        res=[]

        for w in queries:
            for d in dictionary:
                if diff(w,d)<=2:
                    res.append(w)
                    break
        return res

