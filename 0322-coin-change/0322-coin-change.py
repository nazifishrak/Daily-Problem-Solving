class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recurse(target, memo):
            temp=[]
            if target==0:
                return 0
            elif target <0:
                return amount+1
            else:
                for c in coins:
                    if target-c in memo:
                        y=memo[target-c]
                    else:
                        y=recurse(target-c,memo)
                        memo[target-c]=y
                    temp.append(y)

                x= min(temp)+1
                temp=[]
                return x
        ans = recurse(amount, {})
        if ans>amount:
            return -1
        return ans
            

        