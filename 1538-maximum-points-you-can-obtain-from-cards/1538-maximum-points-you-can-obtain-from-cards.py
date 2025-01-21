class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # [1,2,3,4,5,6,1]

        lsum=0
        rsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        maxSum=lsum
        lp=k-1
        rp=len(cardPoints)-1
        while lp>=0:
            lsum-=cardPoints[lp]
            lp-=1
            rsum+=cardPoints[rp]
            rp-=1
            maxSum=max(maxSum, lsum+rsum)
        return maxSum



        
        
        