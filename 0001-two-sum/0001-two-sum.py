class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i,n in enumerate(nums):
            ntf=target-n
            if ntf in map and map[ntf]!=i:
                return [i, map[ntf]]
            else:
                map[n]=i




            