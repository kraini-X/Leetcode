class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        from collections import defaultdict
        count=0
        n=len(nums)

        for i in range(n):
            distinct=[]
            freq=defaultdict(int)

            for j in range(i,n):
                x=nums[j]

                if x not in freq:
                    distinct.append(x)

                freq[x]+=1
                flag=True
                for k in range(len(distinct)):
                    if freq[distinct[k]]!=k+1:
                        flag=False
                        break
                if flag:
                    count+=1
        return count



        
                
