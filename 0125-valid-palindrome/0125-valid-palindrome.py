class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()

        s = "".join(filter(str.isalnum, s))

        def pal(n, start, end):
            if start >= end:  
                return True
            if n[start] != n[end]: 
                return False
            return pal(n, start + 1, end - 1)  

        return pal(s, 0, len(s) - 1)
