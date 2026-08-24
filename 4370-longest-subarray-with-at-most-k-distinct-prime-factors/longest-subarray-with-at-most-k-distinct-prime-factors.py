class Solution:

    def longestSubarray(self, nums: list[int], k: int) -> int:
        factor_map = {}
        for num in set(nums):
            factors = set()
            val = num
            
            # Factor 2
            if val % 2 == 0:
                factors.add(2)
                while val % 2 == 0:
                    val //= 2
                    
            # Odd factors
            d = 3
            while d * d <= val:
                if val % d == 0:
                    factors.add(d)
                    while val % d == 0:
                        val //= d
                d += 2
                
            if val > 1:
                factors.add(val)
                
            factor_map[num] = factors
        
        l=0
        n=len(nums)
        factor_freq=defaultdict(int)
        ans=float('-inf')
        for r in range(n):
            for factor in factor_map[nums[r]]:
                factor_freq[factor]+=1
            
            while len(factor_freq)>k:
                for factor in factor_map[nums[l]]:
                    factor_freq[factor]-=1
                    
                    if factor_freq[factor]==0:
                        del factor_freq[factor]
                l+=1
            
            if len(factor_freq)<=k:
                ans=max(ans,r-l+1)
        return ans if ans!=float('-inf') else 0
            


        