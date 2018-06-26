# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        nxt = head
        prv = head
        
        if(head == None or head.next == None):
            return head
        
        head = head.next
        
        while nxt != None:
            first = nxt
            second = first.next
            if(second != None):
                nxt = second.next
                prv.next = second
                first.next = nxt
                second.next = first
                
                prv = first
            else:
                nxt = None
                
        return head