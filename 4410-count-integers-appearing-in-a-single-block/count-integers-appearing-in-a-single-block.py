class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        from collections import Counter
    
        freq=Counter(nums)
        n = len(nums)
        i = 0
        count=0
        while i < n:
            j = i

            while j < n and nums[j] == nums[i]:
                j += 1
            
            if j-i==freq[nums[i]]:
                count+=1
            
            i=j
        return count


            
            
        
