from heapq import heapify
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array using heap
        """

        heap=nums[0:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            if i>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
            else:
                continue

        return heap[0]

