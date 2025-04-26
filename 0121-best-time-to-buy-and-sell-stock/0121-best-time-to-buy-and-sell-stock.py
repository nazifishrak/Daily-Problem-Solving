class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        msf=0
        left=0
        right=1
        while right<len(prices):
            if prices[left]>=prices[right]:
                left=right
                right+=1
            else:
                
                diff=prices[right]-prices[left]
                right+=1
                if diff>msf:
                    msf=diff
        return msf
                    
        
        