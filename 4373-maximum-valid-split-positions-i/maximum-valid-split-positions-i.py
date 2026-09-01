class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:

        import math
        n=len(nums)
        def calc(nums):
            n = len(nums)

            prefix = [0] * n
            suffix = [0] * n

            # Prefix GCD
            prefix[0] = nums[0]

            for i in range(1, n):
                prefix[i] = gcd(prefix[i - 1], nums[i])

            # Suffix GCD
            suffix[n - 1] = nums[n - 1]

            for i in range(n - 2, -1, -1):
                suffix[i] = gcd(suffix[i + 1], nums[i])
            count=0
            for i in range(n-1):
                
                if prefix[i]==suffix[i+1]:
                    count+=1
            return count
                        
        
        ans=calc(nums)

        for i in range(n):
            arr=nums[:i]+nums[i+1:]
            ans=max(ans,calc(arr))
        return ans

            



        