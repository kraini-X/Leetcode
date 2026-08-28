class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        prefix=[0]*n
        suffix=[0]*n
        if customers[0]=="N":
            prefix[0]=1
        
        if customers[n-1]=="Y":
            suffix[n-1]=1
        
        for i in range(1,n):
            if customers[i]=="N":
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]
        
        for i in range(n - 2, -1, -1):
            if customers[i] == "Y":
                suffix[i] = suffix[i + 1] + 1
            else:
                suffix[i] = suffix[i + 1]
        
        minm = float('inf')

        ans = 0

        # closing at 0
        penalty = suffix[0]

        if penalty < minm:
            minm = penalty
            ans = 0

        # closing at 1 ... n-1
        for i in range(n - 1):
            penalty = prefix[i] + suffix[i + 1]

            if penalty < minm:
                minm = penalty
                ans = i + 1

        # closing at n
        penalty = prefix[n - 1]

        if penalty < minm:
            minm = penalty
            ans = n

        return ans            