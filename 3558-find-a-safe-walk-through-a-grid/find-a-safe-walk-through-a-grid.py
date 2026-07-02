class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        import heapq
        m=len(grid)
        n=len(grid[0])
        damage=[[float('inf')]*n for _ in range(m)]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        damage[0][0]=grid[0][0]
        pq=[(grid[0][0],0,0)]
        h=health
        while pq:
            d,r,c=heapq.heappop(pq)
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n:
                    newDamage=d+grid[nr][nc]
                    
                    if newDamage<damage[nr][nc] and newDamage<health:
                        damage[nr][nc]=newDamage
                        heapq.heappush(pq,(newDamage,nr,nc))

        if damage[m-1][n-1]<h:
            return True
        return False