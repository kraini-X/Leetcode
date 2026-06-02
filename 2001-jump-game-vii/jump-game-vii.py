class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        from collections import deque
        q=deque([0])
        n=len(s)
        howFar=0
        visited=[False]*n
        while q:
            for _ in range(len(q)):
                i=q.popleft()
                if i==n-1:
                    return True
                
                start=max(i+minJump,howFar+1)
                end=min(n-1,i+maxJump)

                for j in range(start,end+1):
                    if s[j]=="0":
                        visited[j]=True
                        q.append(j)
                howFar=end
        return False


        