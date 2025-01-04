class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        s_list=[c for c in s]
        print(s_list)
        for i, c in enumerate(s_list):
            if c =="(":
                stack.append(i)
            elif c==")" and stack !=[]:
                stack.pop(-1)
            elif c==")":
                s_list[i]=""
            else:
                continue

        for i in range(len(stack)):
            s_list[stack[i]]=""
        return "".join(s_list)
                
        