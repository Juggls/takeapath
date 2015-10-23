# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        point1 = head
        point2 = head
        
        while(point2 and point2.next):
            point2 = point2.next.next

            point1 = point1.next

            if (point1 is point2):
                return True
        
        return False
        