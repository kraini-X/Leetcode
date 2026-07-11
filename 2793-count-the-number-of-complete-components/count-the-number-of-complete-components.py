class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        from collections import defaultdict
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=[False]*n
        def dfs(node,visited):
            visited[node]=True
            nodes=1
            edges=len(graph[node])
            for nei in graph[node]:
                if not visited[nei]:
                    n,e=dfs(nei,visited)
                    nodes+=n
                    edges+=e
            return [nodes,edges]
        #print(dfs(0,visited))
        
        ans=0
        for i in range(n):
            if not visited[i]:
                nodes,edg=dfs(i,visited)
                edg//=2
                if edg==nodes*(nodes-1)//2:
                    ans+=1
        return ans
                

        