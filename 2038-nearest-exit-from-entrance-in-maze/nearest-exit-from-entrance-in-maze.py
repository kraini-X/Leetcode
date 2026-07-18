class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque
        m=len(maze)
        n=len(maze[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False]*n for _ in range(m)]
        visited[entrance[0]][entrance[1]]=True
        q=deque([(entrance[0],entrance[1])])
        level=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()

                if [r,c]!=entrance and (r==0 or r==m-1 or c==0 or c==n-1):
                    return level
                
                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc

                    if 0<=nr<m and 0<=nc<n and maze[nr][nc]=="." and not visited[nr][nc]:
                        visited[nr][nc]=True
                        q.append((nr,nc))
            level+=1
        return -1
                
