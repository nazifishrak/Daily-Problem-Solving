class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s): 
            return s

        r = 0
        down = True
        mat = [""] * numRows  

        for i in s:
            mat[r] += i  
            if r == 0: 
                down = True
            elif r == numRows - 1:  
                down = False
            
            if down:
                r+=1
            else:
                r-=1
        
        return "".join(mat)  