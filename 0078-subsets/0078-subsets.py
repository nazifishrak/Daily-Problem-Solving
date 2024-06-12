class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        subsets = [[]]
        for i in nums:
            subsets += [j + [i] for j in subsets]
        return subsets

            
            

