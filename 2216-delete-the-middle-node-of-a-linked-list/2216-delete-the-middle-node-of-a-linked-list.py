# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            # If there's no node or only one node, return None (empty list)
            return None
        curr = head
        n=0
        while(curr != None):
            n+=1
            curr = curr.next
        curr=head

        mid = n//2
        for i in range(mid-1):
            curr=curr.next
        nextNode = curr.next
        curr.next = nextNode.next
        del nextNode

        return head

        