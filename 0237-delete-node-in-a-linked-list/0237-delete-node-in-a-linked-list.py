# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # I am swapping the 3 and 4 and then deleting as I can technically only delete the next
        curr_val = node.val
        next_val = node.next.val
        node.val = next_val
        node.next.val = curr_val
        node.next = node.next.next

        # 5->3->4->6