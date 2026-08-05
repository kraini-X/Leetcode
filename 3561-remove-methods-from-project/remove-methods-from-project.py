class Solution:
    def remainingMethods(self, n: int, k: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)

        sus=[False]*n

        def dfs(node):
            sus[node]=True

            for nei in graph[node]:
                if not sus[nei]:
                    dfs(nei)
        
        dfs(k)
        ans=[]
        for u, v in edges:
            if not sus[u] and sus[v]:
                return list(range(n))


        for i in range(n):
            if not sus[i]:
                ans.append(i)

        return ans