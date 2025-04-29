class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # obj={}
        # for num in nums:
        #     if num in obj:
        #         return True
        #     else:
        #         obj[num]=1
        
        # return False

        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False


        