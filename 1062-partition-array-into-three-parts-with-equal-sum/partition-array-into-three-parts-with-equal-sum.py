class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n=len(arr)
        sums=sum(arr)

        if sums%3!=0:
            return False

        target=sums//3

        curr=0
        parts=0
        for i in range(n):
            curr+=arr[i]

            if curr==target:
                parts+=1
                curr=0
        return parts>=3
        

        