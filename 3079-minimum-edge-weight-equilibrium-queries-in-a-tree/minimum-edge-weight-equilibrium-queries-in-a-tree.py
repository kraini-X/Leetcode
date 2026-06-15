class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        cols=n.bit_length() + 1
        up=[[-1]*cols for _ in range(n)]
        depth=[0]*n
        f = [[0] * 27 for _ in range(n)]

        def dfs(curr,parent):
            up[curr][0]=parent
            
            
            for nei,w in graph[curr]:
                if nei==parent:
                    continue
                depth[nei]=depth[curr]+1
                

                for i in range(27):
                    f[nei][i]=f[curr][i]
                f[nei][w]+=1
                dfs(nei,curr)
        dfs(0,-1)

        def lca(u,v,up):
            if depth[u]<depth[v]:
                u,v=v,u
            diff=depth[u]-depth[v]

            for j in range(cols):
                if diff&(1<<j):
                    u=up[u][j]
            if u==v:
                return u
            
            for j in range(cols-1,-1,-1):
                if up[u][j]==-1:
                    continue
                if up[u][j]!=up[v][j]:
                    u=up[u][j]
                    v=up[v][j]
            return up[u][0]

        #up table construction
        for j in range(1,cols):
            for node in range(n):
                if up[node][j-1]!=-1:
                    up[node][j]=up[up[node][j-1]][j-1]

        #process queries
        res=[]
        for u,v in queries:
            lc=lca(u,v,up)
            dist=depth[u]+depth[v]-2*(depth[lc])

            max_freq=0
            for i in range(27):
                diff=f[u][i]+f[v][i]-2*(f[lc][i])
                max_freq=max(max_freq,diff)
            res.append(dist-max_freq)
        return res
            
        



        
        