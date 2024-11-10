class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array using quickselect.
        
        Args:
            nums: List[int] - input array
            k: int - k value for kth largest element
            
        Returns:
            int - kth largest element
        """
        def quick_select(nums, k):
            if not nums:
                return None
            if len(nums) == 1:
                return nums[0]
            
            pivot = nums[len(nums) // 2]  # Choose middle element as pivot to avoid worst case
            left_part = [n for n in nums if n > pivot]
            right_part = [n for n in nums if n < pivot]
            equal_part = [n for n in nums if n == pivot]
            
            if k <= len(left_part):
                return quick_select(left_part, k)
            elif k <= len(left_part) + len(equal_part):
                return pivot
            else:
                return quick_select(right_part, k - len(left_part) - len(equal_part))
        
        return quick_select(nums, k)