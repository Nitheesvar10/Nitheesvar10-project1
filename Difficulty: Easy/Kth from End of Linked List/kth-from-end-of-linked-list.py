""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        # code here
        slow=head 
        fast=head
        count=0
        for _ in range(k):
            if fast is None:
                return -1
            fast=fast.next 
            count+=1
            
        while fast:
            slow=slow.next
            fast=fast.next 
            
        
        
        return slow.data 
        
    
            
            