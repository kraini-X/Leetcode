class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        from collections import defaultdict
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        n=len(nums)
        subsets=[]
        def solve(i,temp):
            if i>=n:
                if temp:
                    subsets.append(temp[:])
                return
            
            temp.append(i)
            solve(i+1,temp)

            temp.pop()
            solve(i+1,temp)
        
        def dfs(node,visited,allowed):

            visited[node]=True

            for nei in graph[node]:
                if nei in allowed and not visited[nei]:
                    dfs(nei,visited,allowed)
        
        solve(0,[])
        count=0
        for sb in subsets:
            sums=0
            visited=[False]*n
            dfs(sb[0],visited,sb)
            for num in sb:
                sums+=nums[num]
            if all(visited[num]==True for num in sb) and sums%2==0:
                count+=1           
        return count


        

        
        


        