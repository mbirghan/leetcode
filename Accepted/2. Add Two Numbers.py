# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        solution = ListNode(0)
        currentNode = solution
        nextNode = None
        left = l1
        right = l2
        overflow = 0
        
        while left != None or right != None or overflow != 0:
            currentNode.next = nextNode
            if(nextNode != None):
                currentNode = nextNode
            if(left == None):
                leftVal = 0
            else:
                leftVal = left.val
                left = left.next
            if(right == None):
                rightVal = 0
            else:
                rightVal = right.val
                right = right.next
            
            solutionVal = leftVal + rightVal + overflow
            overflow = solutionVal/10
            solutionVal = solutionVal % 10
            
            nextNode = ListNode(0)
            
            currentNode.val = solutionVal
        
        return solution