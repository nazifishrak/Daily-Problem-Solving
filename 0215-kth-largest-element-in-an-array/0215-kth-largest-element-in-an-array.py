class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [3,2,1,5,6,4]

        def quick_select(nums):
            if nums==[]:
                return []
            else:
                p = nums[0]
                left_part=filter(lambda n: n<p, nums)
                right_part=filter(lambda n: n>p, nums)
                equal_part=filter(lambda n: n==p, nums)
                return quick_select(left_part)+equal_part+quick_select(right_part)
        
        return quick_select(nums)[len(nums)-k]