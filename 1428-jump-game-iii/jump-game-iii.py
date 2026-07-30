class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)

        def dfs(idx,visited):

            if idx>=n or idx<0:
                return False
            
            if arr[idx]==0:
                return True
            visited.add(idx)

            if idx+arr[idx] not in visited:
                if dfs(idx+arr[idx],visited):
                    return True

            if idx-arr[idx] not in visited:
                if dfs(idx-arr[idx],visited):
                    return True
            
            return False
        visited=set()
        return dfs(start,visited)

            

        