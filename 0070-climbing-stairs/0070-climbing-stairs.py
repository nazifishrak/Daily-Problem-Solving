class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}


        def ways(i):
            if i in memo:
                return memo[i]
            if (i>=n):
                return 1
            else:
                
                x = ways(i+1)
                y = ways(i+2)
                memo[i]= x+y
                return memo[i]
        return ways(1)
