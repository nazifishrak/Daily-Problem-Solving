class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[x for x in nums]
        for i,n in enumerate(nums):
            if i==0:
                prefix[i]=1
            else:
                prefix[i]=prefix[i-1]*nums[i-1]

        postfix=[x for x in nums]
        
        for i in range(len(nums)-1,-1,-1):
            if i ==len(nums)-1:
                postfix[i]=1
            else:
                postfix[i]=postfix[i+1]*nums[i+1]

        i=0
        while i<len(nums):
            nums[i]=prefix[i]*postfix[i]
            i+=1

        return nums



        