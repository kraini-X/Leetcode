class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        t=""
        count=0
        for ch in s:
            if ch==y or ch!=x:
                t+=ch
            elif ch==x:
                count+=1
        while count!=0:
            t+=x
            count-=1
        return t
        