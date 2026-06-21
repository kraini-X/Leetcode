class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            sums=0
            for j in range(i,n):
                sums+=nums[j]
                st=str(sums)
                if int(st[0])==x and int(st[-1])==x:
                    count+=1
        return count
        