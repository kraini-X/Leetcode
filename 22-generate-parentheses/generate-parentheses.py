class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def isValid(curr):
            stack=[]
            for ch in curr:
                if stack:
                    if ch==")" and stack[-1]=="(":
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
            if stack==[]:
                return True
            return False
        
        def solve(temp):
            if len(temp)==2*n:
                if isValid(temp):
                    res.append("".join(temp))
                return
            
            temp.append("(")
            solve(temp)
            temp.pop()

            temp.append(")")
            solve(temp)
            temp.pop()
        solve([])
        return res