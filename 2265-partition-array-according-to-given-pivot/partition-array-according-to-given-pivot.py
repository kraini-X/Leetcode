class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        greater=[]
        n=len(nums)
        res=[0]*n
        count=0
        for num in nums:
            if num==pivot:
                count+=1
            if num<pivot:
                less.append(num)
            elif num>pivot:
                greater.append(num)
        print(count)
        print(less)
        print(greater)
        idx=0
        j=0
        for i in range(len(less)):
            res[i]=less[i]
            idx=i
        if less:
            while count>0:
                res[idx+1]=pivot
                idx+=1
                count-=1
            
            while idx+1<n and j<len(greater):
                res[idx+1]=greater[j]
                idx+=1
                j+=1
                
        else:
            while count>0:
                res[idx]=pivot
                idx+=1
                count-=1
            
            while idx<n and j<len(greater):
                res[idx]=greater[j]
                idx+=1
                j+=1

        print(idx)
        
        return res
        


        