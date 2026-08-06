class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degrees=[0]*(n+1)
        graph=defaultdict(set)
        ans=float('inf')
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degrees[u]+=1
            degrees[v]+=1
        
        for u in range(n):
            for v in graph[u]:
                if u<v:
                    common=graph[u] & graph[v]

                    for w in common:
                        if v<w:
                            ans=min(
                                ans,
                                degrees[u]+degrees[v]+degrees[w]-6
                            )
            
        return ans if ans!=float('inf') else -1
        

        
