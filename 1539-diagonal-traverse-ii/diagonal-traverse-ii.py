class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import deque
        q = deque([(0, 0)])
        ans = []
        n=len(nums)
        visited=set()
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()

                ans.append(nums[r][c])

                if r+1<n and c<len(nums[r+1]) and (r+1,c) not in visited:
                    visited.add((r+1,c))
                    q.append((r+1,c))
                
                if c+1<len(nums[r]) and (r,c+1) not in visited:
                    visited.add((r,c+1))
                    q.append((r,c+1))
        return ans

        