""" Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        pre=None
        cur=head
        while cur:
            temp=cur.next 
            cur.next=pre
            pre=cur
            cur=temp
            
        return pre