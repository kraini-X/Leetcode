class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        from collections import deque
        dirs = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]
        visited=[[False]*8 for _ in range(8)]
        q = deque([[start[0], start[1]]])
        moves=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()

                if [r,c]==target and moves%2==0:
                    return True
                
                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc

                    if 0<=nr<8 and 0<=nc<8:
                        if not visited[nr][nc]:
                            visited[nr][nc]=True
                            q.append([nr,nc])
            moves+=1
        return False

