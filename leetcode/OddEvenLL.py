    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        #test
        def oddEvenList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if head == None:
                return 
            
            odd = head
            even_h = head.next
            even = head.next
            
            while(even != None and even.next != None):
                odd.next = even.next
                odd = odd.next
                even.next = even.next.next
                even = even.next
            odd.next = even_h
            
            return head
                
                