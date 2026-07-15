class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        even,odd=0,0
        for i in range(1,2*n+1):
            if i%2==0:
                even+=1
            else:
                odd+=1
        return math.gcd(even,odd)

        