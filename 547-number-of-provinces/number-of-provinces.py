class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)

        graph=[[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1 and i!=j:
                    graph[i].append(j)
                    graph[j].append(i)

        visited=[False]*(n+1)

        def dfs(node):
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        
        count=0
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
                
        return count
