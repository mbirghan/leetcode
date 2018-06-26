# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseListRecursive(head, None)
        
    def reverseListRecursive(self, head, prevHead):
        if(head == None):
            return prevHead
        else:
            newHead = head.next
            head.next = prevHead
            nextHead = self.reverseListRecursive(newHead, head)
            return nextHead
            
        
        