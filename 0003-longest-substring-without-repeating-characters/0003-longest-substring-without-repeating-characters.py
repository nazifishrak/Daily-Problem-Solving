class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        if len(s)==1:
            return 1
        slow,fast=0,0
        max_len =0
        while fast+1<len(s):
            if s[fast+1] in s[slow:fast+1]:
                slow+=1
                max_len = max(max_len, fast-slow+1) 
            else:
                fast+=1
                max_len = max(max_len, fast-slow+1)

        return max_len
            
        