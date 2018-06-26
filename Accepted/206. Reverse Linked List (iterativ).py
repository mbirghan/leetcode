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
        currentHead = None
        
        while head != None:
            tmpNode = head.next
            head.next = currentHead
            currentHead = head
            head = tmpNode
            
        return currentHead
        
        