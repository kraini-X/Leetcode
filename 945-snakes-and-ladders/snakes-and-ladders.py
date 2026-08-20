class Solution:
    from collections import deque
    def pos(self,x,n):
            r = (x - 1) // n
            c = (x - 1) % n

            if r % 2:
                c = n - 1 - c

            r = n - 1 - r

            return [r,c]
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        q=deque([1])
        visited=set([1])

        level=0
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr==n**2:
                    return level
                for nxt in range(curr+1,min(curr+6,n**2)+1):
                    r,c=self.pos(nxt,n)

                    if board[r][c]!=-1:
                        if board[r][c] not in visited:
                            q.append(board[r][c])
                            visited.add(board[r][c])
                    else:
                        
                        if nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)
            level+=1
        return -1



        
        
