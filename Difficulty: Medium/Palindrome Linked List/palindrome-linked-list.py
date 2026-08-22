'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next 
            slow=slow.next
            
        prev=None
        cur=slow 
        while cur:
            temp=cur.next 
            cur.next=prev
            prev=cur
            cur=temp
        
        while prev and head:
            if prev.data !=head.data:
                return False 
                
            prev=prev.next 
            head=head.next 
            
        return True 
        
        
        