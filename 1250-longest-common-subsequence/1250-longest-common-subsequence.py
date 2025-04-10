class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # banana
        # nana

        def helper(i,j,memo):
            key=str(i)+"_"+str(j)
            if key in memo:
                return memo[key]

            if i>=len(text1) or j>=len(text2):
                result = 0
                memo[key]=0

                return memo[key]
            if text1[i]==text2[j]:
                result= 1+helper(i+1,j+1,memo)
                memo[key]=result
            else:
                result = max(helper(i,j+1,memo), helper(i+1,j,memo))
                memo[key]=result
            return memo[key]


        return helper(0,0,{})

        