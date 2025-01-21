class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [[0,1,2,0],
         [3,4,5,2],
         [1,3,1,5]]
        """
        rows=set()
        cols=set()
        for r,row in enumerate(matrix):
            for c, col in enumerate(row):
                if col==0:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            for i in range(len(matrix[0])):
                matrix[r][i]=0
                
        for c in cols:
            for i in range(len(matrix)):
                matrix[i][c]=0


        



                


        

        