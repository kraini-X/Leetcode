class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        n=len(nums)
        memo={}
        def solve(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[(i)]

            alice=nums[i]-solve(i+1)            

            if i+1<n:
                alice=max(alice,nums[i]+nums[i+1]-solve(i+2))
            
            if i+2<n:
                alice=max(alice,nums[i]+nums[i+1]+nums[i+2]-solve(i+3))
            memo[(i)]=alice
            return alice
        
        alice=solve(0)

        if alice<0:
            return "Bob"
        elif alice>0:
            return "Alice"
        else:
            return "Tie"