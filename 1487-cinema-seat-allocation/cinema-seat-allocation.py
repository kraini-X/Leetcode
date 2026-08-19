class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        def isAvail(row,seat):
            if seat in mp[row]:
                return False
            return True

        from collections import defaultdict
        mp=defaultdict(list)

        for r,seat in reservedSeats:
            if 2 <= seat <= 9:
                mp[r].append(seat)
    
        ans=(n-len(mp))*2


        for row in mp:
            grpA=isAvail(row,2) and isAvail(row,3) and isAvail(row,4) and isAvail(row,5)
            grpB=isAvail(row,4) and isAvail(row,5) and isAvail(row,6) and isAvail(row,7)
            grpC=isAvail(row,6) and isAvail(row,7) and isAvail(row,8) and isAvail(row,9)
        
            if grpA and grpC:
                ans+=2
            
            elif grpA or grpB or grpC:
                ans+=1
        return ans

