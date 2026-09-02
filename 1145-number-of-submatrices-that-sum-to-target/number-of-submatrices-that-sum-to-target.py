class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # STEP 1:
        # Make every row cumulative
        for row in range(rows):
            for col in range(1, cols):
                matrix[row][col] += matrix[row][col - 1]
        
        ans=0
        for startCol in range(cols):
            for j in range(startCol,cols):
                mp=defaultdict(int)
                mp[0]=1
                prefix=0
                for row in range(rows):
                    if startCol > 0:
                        current = matrix[row][j] - matrix[row][startCol - 1]
                    else:
                        current = matrix[row][j]
                    prefix+=current

                    ans+=mp[prefix-target]
                    mp[prefix]+=1
        return ans



        