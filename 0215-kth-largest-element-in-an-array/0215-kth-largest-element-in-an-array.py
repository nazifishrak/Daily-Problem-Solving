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
                left_part, right_part, equal_part =[],[],[]
                for i in nums:
                    if i<p:
                        left_part.append(i)
                    elif i==p:
                        equal_part.append(i)
                    else:
                        right_part.append(i)

                return quick_select(left_part)+equal_part+quick_select(right_part)
        
        return quick_select(nums)[len(nums)-k]