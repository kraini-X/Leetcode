class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total=0
        m=len(matrix)
        n=len(matrix[0])
        neg=0
        min_num=float('inf')
        for i in range(m):
            for j in range(n):
                total+=abs(matrix[i][j])
                min_num=min(min_num,abs(matrix[i][j]))
                if matrix[i][j]<0:
                    neg+=1
        
        if neg%2!=0:
            return total-2*min_num
        else:
            return total


        
        