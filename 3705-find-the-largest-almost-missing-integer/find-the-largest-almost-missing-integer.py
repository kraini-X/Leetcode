class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)

        l=0
        r=k-1
        freq={num:0 for num in nums}
        seen=set()
        for i in range(l,r+1):
            
            if nums[i] not in seen:
                seen.add(nums[i])
                freq[nums[i]]+=1
        
        #print(freq)
        for r in range(k,n):
            l+=1
            seen=set()
            for i in range(l,r+1):
                
                if nums[i] not in seen:
                    seen.add(nums[i])
                    freq[nums[i]]+=1
    
            
        
        ans=float('-inf')
        print(freq)
        for key,val in freq.items():
            if val==1:
                ans=max(ans,key)
        return ans if ans!=float('-inf') else -1
