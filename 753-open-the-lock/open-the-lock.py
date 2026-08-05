class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        visited=set()

        visited.add("0000")
        q=deque(["0000"])
        level=0
        while q:
            for _ in range(len(q)):
                pattern=q.popleft()
                
                if pattern in deadends:
                    continue
                
                if pattern==target:
                    return level
                
                for i in range(4):
                    digit=int(pattern[i])
                    for move in list((-1,+1)):
                        newDigit=(digit+move)%10

                        newPattern=pattern[:i]+str(newDigit)+pattern[i+1:]

                        if newPattern not in visited and newPattern not in deadends:
                            visited.add(newPattern)
                            q.append(newPattern)
            level+=1
        return -1




        