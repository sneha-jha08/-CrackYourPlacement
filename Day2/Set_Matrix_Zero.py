class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows=[]
        cols=[]
        R=len(matrix)
        C=len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
# Iterate over the array once again and using the rows and cols sets, update the elements
       
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
