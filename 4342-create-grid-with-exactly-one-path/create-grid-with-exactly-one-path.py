class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        grid=[["#"]*n for _ in range(m)]
        for col in range(n):
            grid[0][col]="."
        
        for row in range(m):
            grid[row][n-1]="."
        
        return [''.join(row) for row in grid]

        
        