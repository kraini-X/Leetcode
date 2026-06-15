class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        import math
        mod=10**9+7
        from collections import defaultdict
        graph=defaultdict(list)
        parent=[-1]*(len(edges)+2)
        dep=[0]*(len(edges)+2)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            #parent[v]=u
        

        def dfs(node, par):
            parent[node] = par

            for nei in graph[node]:
                if nei != par:
                    dep[nei] = dep[node] + 1
                    dfs(nei, node)

        dfs(1, -1)
        
        def lca(u,v,ancestor,depth):
            if depth[u]<depth[v]:
                u,v=v,u
            diff = depth[u] - depth[v]
            cols=len(ancestor[0])

            for j in range(cols):
                if diff & (1 << j):
                    u = ancestor[u][j]
                        
            if u == v:          # ← critical early exit
                return u
            for j in range(cols-1,-1,-1):
                if ancestor[u][j]!=-1 and ancestor[u][j]!=ancestor[v][j]:
                    u=ancestor[u][j]
                    v=ancestor[v][j]
            return ancestor[u][0]
        
        
        n=len(edges)+1
        cols = max(1, n.bit_length())
        ancestor=[[-1]*cols for _ in range(n+1)]

        for i in range(n+1):
            ancestor[i][0]=parent[i]
        
        for j in range(1,cols):
            for node in range(n+1):
                if ancestor[node][j-1]!=-1:
                    ancestor[node][j]=ancestor[ancestor[node][j-1]][j-1]
                    
        res=[]
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (2 * pow2[i-1]) % (10**9 + 7)

        for u,v in queries:
            lc=lca(u,v,ancestor,dep)
            val=dep[u]+dep[v]-2*(dep[lc])
            if val==0:
                res.append(0)
            else:
                res.append(pow2[val-1])
        return res





        


        
        