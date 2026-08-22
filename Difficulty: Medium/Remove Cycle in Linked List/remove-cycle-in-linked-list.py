''' Structure of Linked List Node
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
'''

class Solution:
    def removeLoop(self, head):
        # code here
        slow=head 
        fast=head
        while fast and fast.next :
            
            slow=slow.next
            fast=fast.next.next 
            
            
            if slow==fast:
                slow=head
                
                
                while slow !=fast:
                    slow=slow.next 
                    fast=fast.next 
                
                while fast.next!=slow:
                    fast=fast.next 
                
                fast.next=None 
            
        return 
                