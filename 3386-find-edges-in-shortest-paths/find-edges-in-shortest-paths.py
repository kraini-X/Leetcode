class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        import heapq
        ans=[]
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        distStart=[float('inf')]*n
        distEnd=[float('inf')]*n


        def dijkstras(start,dist):
            pq=[(0,start)]
            dist[start]=0
            while pq:
                wt,node=heapq.heappop(pq)
                if wt>dist[node]:
                    continue
                for nei,w in graph[node]:
                    newVal=wt+w

                    if newVal<dist[nei]:
                        dist[nei]=newVal
                        heapq.heappush(pq,(newVal,nei))
        dijkstras(0,distStart)
        dijkstras(n-1,distEnd)
        shortest=distStart[n-1]
        if shortest == float('inf'):
            return [False] * len(edges)

        for u,v,w in edges:
            if (distStart[u] + w + distEnd[v] == distStart[n-1] or
    distStart[v] + w + distEnd[u] == distStart[n-1]):
                ans.append(True)
            else:
                ans.append(False)
        return ans