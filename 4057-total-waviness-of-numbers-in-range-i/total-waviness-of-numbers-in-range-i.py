class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x):
            nums=[]
            st=str(x)
            for ch in st:
                nums.append(int(ch))
            peaks=0
            valleys=0
            n=len(nums)
            if n<3:
                return 0
            for i in range(1,n-1):
                if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                    peaks+=1
                elif nums[i]<nums[i+1] and nums[i]<nums[i-1]:
                    valleys+=1
            return peaks+valleys
        
        ans=0
        for n in range(num1,num2+1):
            ans+=waviness(n)
        return ans
                
                

