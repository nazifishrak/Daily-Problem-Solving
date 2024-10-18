class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        balance = 0
        index = []

        for p1 in range(len(s)):
            if s[p1] == "(":
                balance += 1
            elif s[p1] == ")":
                if balance == 0:
                    index.append(p1)  
                else:
                    balance -= 1
        

        balance = 0
        for p1 in range(len(s)-1, -1, -1):
            if s[p1] == "(":
                if balance == 0:
                    index.append(p1)  
                else:
                    balance -= 1
            elif s[p1] == ")":
                balance += 1

        output = ""
        for i in range(len(s)):
            if i not in index:
                output += s[i]

        return output
