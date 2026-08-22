'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        if head is None:
            head=Node(x)
            return head 
        cur=head
        while cur.next is  not None:
            cur=cur.next
            
        cur.next=Node(x)
        
        return head 
        
        
        