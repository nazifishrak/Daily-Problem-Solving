class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]
        invalid=set()
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if len(stack) !=0:
                    stack.pop()
                else:
                    invalid.add(i)
        
        for i in stack:
            invalid.add(i)

        output =""

        for i,char in enumerate(s):
            if i not in invalid:
                output+=char

        return output
            

    
