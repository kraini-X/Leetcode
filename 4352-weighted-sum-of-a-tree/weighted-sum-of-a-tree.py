class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        from collections import deque
        n=len(parent)
        tree=defaultdict(list)
        q=deque()

        for i in range(1,n):
            tree[i].append(parent[i])
            tree[parent[i]].append(i)
        
        def height(node,visited):
            depth=0
            visited[node]=True

            for nei in tree[node]:
                if not visited[nei]:
                    depth=max(depth,1+height(nei,visited))
            return depth
        

        visited=[False]*n
        h=1+height(0,visited)
        q.append(0)
        ans=0
        level=1
        visited=[False]*n
        visited[0] = True
        while q:
            for _ in range(len(q)):
                node=q.popleft()

                ans+=nums[node]*(h-level+1)

                for nei in tree[node]:
                    if not visited[nei]:
                        visited[nei]=True
                        q.append(nei)
            level+=1
        return ans

