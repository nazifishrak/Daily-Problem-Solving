class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        # "((()))"
        dic={"(":")", "{":"}", "[":"]"}
        if s=="":
            return True
        else:
            for c in s:
                if c=="(" or c=="{" or c=="[":
                    stack.append(c)
                else:
                    if stack==[]:
                        return False
                    removed=stack.pop(-1)
                    if dic[removed] == c:
                        continue
                    else:
                        return False
            if stack==[]:

                return True
            else:
                return False
        


        