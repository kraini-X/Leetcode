class Solution:
    def maxDistance(self, moves: str) -> int:

        count=0
        x,y=0,0
        for ch in moves:
            if ch=='U':
                y+=1
            elif ch=='D':
                y-=1
            elif ch=="L":
                x-=1
            elif ch=="R":
                x+=1
            elif ch=="_":
                count+=1

        xAb=abs(x)
        yAb=abs(y)
        ifX=False
        while count!=0:
            if ifX:
                xAb+=1
            else:
                yAb+=1
            count-=1
            ifX= not ifX

        
        return abs(0-xAb)+abs(0-yAb)


