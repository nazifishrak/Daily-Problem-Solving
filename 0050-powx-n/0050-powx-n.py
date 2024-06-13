class Solution(object):
    def myPow(self, x, n):
        if n<0:
            n = abs(n)
            x=1/x
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow_helper(x, n):

            if n==0:
                return 1
            
            if n%2==0:
                partial=pow_helper(x,n/2)
                return partial*partial
            else:
                partial=pow_helper(x,n/2)
                return x*partial*partial

        return pow_helper(x,n)

