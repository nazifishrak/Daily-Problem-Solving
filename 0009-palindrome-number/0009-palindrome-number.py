class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        def length(n):
            counter = 0
            while n != 0:
                n = n // 10
                counter += 1
            return counter

        def pal(n,l):
            if x<0:
                return False
            if l<=1:
                return True
            f = n//(10**(l-1))
            la = n%10
            if f != la:
                return False
            else:
                trunc = (n%(10**(l-1)))//10
                return pal(trunc,l-2)

        return pal(x,length(x))


            
        