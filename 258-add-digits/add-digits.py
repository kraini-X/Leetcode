class Solution:
    def addDigits(self, num: int) -> int:
        def solve(n):
            if n==0:
                return 0

            
            return n%10+solve(n//10)
        if num<10:
            return num

        return self.addDigits(solve(num))
        
        