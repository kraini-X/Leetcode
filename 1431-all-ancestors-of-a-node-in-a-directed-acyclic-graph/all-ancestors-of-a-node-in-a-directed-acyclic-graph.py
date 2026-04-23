class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict,deque
        graph=defaultdict(list)
        indegree=[0]*n
        ancestors = [set() for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            for nei in graph[node]:
                ancestors[nei].update(ancestors[node])
                ancestors[nei].add(node)

                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        ancestors=[sorted(set(lst)) for lst in ancestors]
        return ancestors
        

        