class Solution:
    def canVisitAllRooms(self, graph: List[List[int]]) -> bool:

        n=len(graph)
        visited=[False]*n
        def dfs(node):
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        dfs(0)
        print(visited)
        if all(s==True for s in visited):
            return True
        else:
            return False
        