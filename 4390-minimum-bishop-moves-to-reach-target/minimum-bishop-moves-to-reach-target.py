class Solution:
    def colour(self,row,column):
        if (row + column) % 2 == 0:
            return 1
        else:
            return 0
        
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        r1,c1=source
        r2,c2=target

        if abs(r1-r2)==abs(c1-c2) and self.colour(r1,c1)==self.colour(r2,c2):
            return 1
        elif self.colour(r1,c1)==self.colour(r2,c2):
            return 2
        else:
            return -1


        
        