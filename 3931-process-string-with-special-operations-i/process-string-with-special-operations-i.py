class Solution:
    def processStr(self, s: str) -> str:
        q=[]
        for ch in s:
            if ord(ch)>=97 and ord(ch)<=122:
                q.append(ch)
            elif ch=="*":
                if q:
                    q.pop(-1)
            elif ch=="#":
                if q:
                    temp=q
                    q=q+temp
            elif ch=="%":
                q=q[::-1]
            print("".join(q))

        return "".join(q)
        