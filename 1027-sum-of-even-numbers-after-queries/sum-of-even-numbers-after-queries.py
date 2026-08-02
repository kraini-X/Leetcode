class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n=len(nums)
        evenSum=0
        for num in nums:
            if num%2==0:
                evenSum+=num
        
        ans=[]
        for val,idx in queries:
            newVal=nums[idx]+val
            
            if nums[idx]%2!=0 and newVal%2==0:
                evenSum+=newVal
            
            elif nums[idx]%2==0 and newVal%2!=0:
                evenSum-=nums[idx]
            
            elif nums[idx]%2==0 and newVal%2==0:
                diff=newVal-nums[idx]
                evenSum+=diff

            ans.append(evenSum)
            nums[idx]=newVal
        return ans
            

                

        
        