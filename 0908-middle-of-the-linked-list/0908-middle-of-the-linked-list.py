# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4
        # 1 2 3 

        pos = 1
        curr = head
        while curr:
            curr = curr.next
            pos+=1

        
        index = pos/2 if pos%2==0 else pos//2 +1
        count=1
        curr=head
        while count<index:
            curr=curr.next
            count+=1
        
        return curr
        
            


        