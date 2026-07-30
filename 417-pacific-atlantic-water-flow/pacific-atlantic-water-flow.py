class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c,visited):
            visited.add((r,c))

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if 0<=nr<m and 0<=nc<n:
                    if heights[nr][nc]>=heights[r][c] and (nr,nc) not in visited:

                        dfs(nr,nc,visited)
        
        atlantic=set()
        pacific=set()
        ans=[]
        for row in range(m):
            dfs(row,0,pacific)
            dfs(row,n-1,atlantic)
        
        for col in range(n):
            dfs(0,col,pacific)
            dfs(m-1,col,atlantic)
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    ans.append([i,j])
        return ans
        

            
            
        