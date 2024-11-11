# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        else:
            curr = head
            prev = None
            while curr.next:
                sec = curr.next
                curr.next=prev
                prev = curr
                curr=sec
                head=curr
        sec = curr.next
        curr.next=prev
        prev = curr
        curr=sec


        return head

        