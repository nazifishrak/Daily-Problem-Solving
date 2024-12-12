import heapq

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        heap = nums[:]
        heapq.heapify(heap)

        curr=1
        msf=1

        old = heapq.heappop(heap)

        while heap:
            new = heapq.heappop(heap)
            if new == old+1:
                curr+=1
                msf=max(msf,curr)
            elif old==new:
                continue
            else:
                curr=1
            old=new
        
        return msf
