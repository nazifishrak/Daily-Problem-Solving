class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo={}
        def helper(pos):
            if pos in memo:
                return memo[pos]
            if (pos>=len(cost)):
                return 0
            else:
                memo[pos]=cost[pos]+min(helper(pos+1), helper(pos+2))
                return memo[pos]

        return min(helper(0),helper(1))
        