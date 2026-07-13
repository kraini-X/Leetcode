class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        from collections import deque
        q = deque(range(1, 10))
        ans=[]

        while q:
            for _ in range(len(q)):
                num=q.popleft()

                if low<=num<=high:
                    ans.append(num)
                
                lastDigit=num%10
                if lastDigit<9:
                    newNum=num*10+(lastDigit+1)
                    q.append(newNum)
        return ans