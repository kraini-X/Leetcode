class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        from math import log2, ceil
        self.cols=ceil(log2(n)+1)
        self.parent=[[-1]*self.cols for _ in range(n)]

        for i in range(n):
            self.parent[i][0]=parent[i]

        for j in range(1,self.cols):
            for node in range(n):
                if self.parent[node][j-1]!=-1:
                    self.parent[node][j]=self.parent[self.parent[node][j-1]][j-1]

        

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.cols):
            if (k&(1<<j)):
                node=self.parent[node][j]
            
            if node==-1:
                return -1
        return node
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)