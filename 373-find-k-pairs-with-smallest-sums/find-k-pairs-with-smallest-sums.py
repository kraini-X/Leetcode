class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        m=len(nums1)
        n=len(nums2)
        start=nums1[0]+nums2[0]
        res=[]
        pq=[(start,0,0)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()
        visited.add((0,0))
        while pq and k:
            sums,r,c=heapq.heappop(pq)
            res.append([nums1[r],nums2[c]])

            for dr,dc in dirs:
                nr=r+dr
                nc=c+dc

                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    val=nums1[nr]+nums2[nc]
                    heapq.heappush(pq,(val,nr,nc))
            k-=1
        return res

