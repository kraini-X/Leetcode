class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict
        graph=defaultdict(list)
        
        for u,v in prerequisites:
            graph[u].append(v)

        def dfs(node,target,visited):
            if node==target:
                return True
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    if dfs(nei,target,visited):
                        return True
            return False
        ans=[False]*len(queries)
        for i in range(len(queries)):
            visited=[False]*n
            src=queries[i][0]
            dest=queries[i][1]
            if dfs(src,dest,visited):
                ans[i]=True
        return ans


        

        