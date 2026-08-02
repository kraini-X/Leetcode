class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        import math
        n=len(nums)
        memo={}
        def solve(idx,op1,op2):
            if idx>=n:
                return 0

            if (idx,op1,op2) in memo:
                return memo[(idx,op1,op2)]
            ans = nums[idx] + solve(idx + 1, op1, op2)
            

            if op1>0:
                option1=math.ceil(nums[idx] / 2) + solve(idx+1,op1-1,op2)
                ans=min(ans,option1)
            
            if op2>0 and nums[idx]>=k:
                option2=nums[idx]-k + solve(idx+1,op1,op2-1)
                ans=min(ans,option2)
            #op1-->op2
            if op1>0 and op2>0:
                x=nums[idx]
                a=math.ceil(x / 2)
                if k<=a:
                    a-=k
                ans=min(ans,a+solve(idx+1,op1-1,op2-1))

                #op2-->op1
                b=x
                if k<=b:
                    b-=k
                ans=min(
                    ans,
                    math.ceil(b / 2) + solve(idx+1,op1-1,op2-1)
                    )
                
            memo[(idx,op1,op2)]=ans
            return ans
        return solve(0,op1,op2)


        