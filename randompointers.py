"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        seenNodes = set()
        while head:


#ALTERNATIVE SOLUTION

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mapping = dict()
        
        mapping = dict()
        def copyNode(n):
            if not n: 
                return n #return if None
            if n in mapping: 
                return mapping[n] #return new node if already in hashtable
            
            mapping[n] = Node(n.val, None, None) #create new Node that is mapped to OG node
            ans = mapping[n] #assign pointer to new Node 
            ans.next = copyNode(n.next) #add next to mapping and assign to new.next
            ans.random = copyNode(n.random) #add random to mapping and assign to new.random
            return ans #return node
        
        return copyNode(head)
        
            