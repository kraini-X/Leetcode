class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])

        def dfs(row,col):
            if row==m:
                return col
            
            if grid[row][col]==1:
                next_col=col+1
                if next_col >= n:
                    return -1
                if grid[row][next_col]==1:
                    return dfs(row+1,next_col)
                return -1

            elif grid[row][col]==-1:
                next_col=col-1
                if next_col<0:
                    return -1
                
                if grid[row][next_col]==-1:
                    return dfs(row+1,next_col)
                return -1
        
        ans=[]
        for c in range(0,n):
            ans.append(dfs(0,c))
        return ans

        