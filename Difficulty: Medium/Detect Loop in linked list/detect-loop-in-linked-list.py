'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        
        slow=head
        fast=head
        while fast and fast.next:
            if fast is None:
                return False
                
            slow=slow.next
            fast=fast.next.next 
            
            if slow==fast:
                return True 
            
    
