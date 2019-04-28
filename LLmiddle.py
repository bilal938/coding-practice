""" 
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i=0
        
        copy=head
        while copy is not None:
            i+=1
            copy = copy.next
        j=0    
        if i%2!=0:
            while j!=i/2:
                head = head.next
                j+=1
            return head
        while j!=(i//2):
            head = head.next
            j+=1
        return head    
            