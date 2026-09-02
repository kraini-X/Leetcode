class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def check(health):
            memo={}
            def solve(i, j, hp):
                if i < 0 or i >= m or j < 0 or j >= n:
                    return False

                hp += grid[i][j]

                if hp <= 0:
                    return False

                # Already reached this cell with better/equal health
                if (i, j) in memo and memo[(i, j)] >= hp:
                    return False

                memo[(i, j)] = hp

                if i == m - 1 and j == n - 1:
                    return True

                return solve(i + 1, j, hp) or solve(i, j + 1, hp)

            return solve(0, 0, health)

        left=1
        right=1200

        while left<=right:
            mid=(left+right)//2

            if check(mid):
                right=mid-1
            else:
                left=mid+1
        return left