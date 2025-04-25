class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        num_set=set(nums)
        l=len(num_set)
        i=0
        while i<=l:
            if i not in num_set:
                return i
            i+=1

        return -1
        
        