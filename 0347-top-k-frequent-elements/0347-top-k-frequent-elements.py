import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

# Dictionary : {1:3, 2:4}
        
        sorted_items=sorted(dic.items(), key=lambda x:x[1], reverse=True)
        ans = [item for item, count in sorted_items[:k]]
        return ans
       

        