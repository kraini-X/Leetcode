class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # 1. Precompute the prefix sum array of size n + 1
        # prefix[0] = 0 accounts for the empty prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
            
        # 2. Count odd and even prefix sums dynamically
        odd_count = 0
        even_count = 0
        ans = 0
        
        for p in prefix:
            if p % 2 != 0:
                # If current prefix sum is odd, it forms an odd subarray 
                # with all previously seen even prefix sums
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                # If current prefix sum is even, it forms an odd subarray 
                # with all previously seen odd prefix sums
                ans = (ans + odd_count) % MOD
                even_count += 1
                
        return ans