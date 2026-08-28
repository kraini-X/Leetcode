class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import deque
        n=len(arr)
        q=deque([0])
        visited=set()
        
        mp=defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)
        
        level=0
        while q:
            for _ in range(len(q)):
                idx=q.popleft()

                if idx==n-1:
                    return level

                if idx+1<n and idx+1 not in visited:
                    visited.add(idx+1)
                    q.append(idx+1)
                
                if idx-1>=0 and idx-1 not in visited:
                    visited.add(idx-1)
                    q.append(idx-1)
                
                for j in mp[arr[idx]]:
                    if j not in visited:
                        visited.add(j)
                        q.append(j)
                mp[arr[idx]] = []
            level+=1
        return -1
                

