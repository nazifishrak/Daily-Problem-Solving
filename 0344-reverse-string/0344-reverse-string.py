class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def str_swap(i,j):
            f = s[i]
            s[i]=s[j]
            s[j]=f
            return s
        def helper(i,j):
            if i>=j:
                return s
            else:
                str_swap(i,j)
                return helper(i+1,j-1)
        helper(0,len(s)-1)
        