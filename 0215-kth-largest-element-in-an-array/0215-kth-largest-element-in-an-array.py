from random import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums==[]:
            return None

        if len(nums)==1:
            return nums[0]
        p=choice(nums)
        l=[x for x in nums if x>p]
        m=[x for x in nums if x==p]
        r=[x for x in nums if x<p]



        if k<=len(l)+len(m) and len(l)<k:
            return p
        elif len(l)>=k:
            return self.findKthLargest(l,k)
        else:
            return self.findKthLargest(r,k-(len(l)+len(m)))

        # 1 2 3 4 5
            
        