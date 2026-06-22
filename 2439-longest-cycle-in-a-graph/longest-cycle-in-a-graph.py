class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        visited=[False]*n
        inRec=[False]*n
        count=[1]*n

        graph=defaultdict(list)
        for u in range(n):
            if edges[u] != -1:
                graph[u].append(edges[u])
        maxm=-1
        def dfs(node):
            nonlocal maxm
            visited[node]=True
            inRec[node]=True

            for nei in graph[node]:
                if not visited[nei]:
                    count[nei]=count[node]+1
                    dfs(nei)
                elif inRec[nei]:
                    inRec[nei]=False
                    maxm=max(maxm,count[node]-count[nei]+1)
            inRec[node]=False
            return -1
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return maxm

        