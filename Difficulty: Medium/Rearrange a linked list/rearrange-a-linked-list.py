""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def rearrangeEvenOdd(self, head):
        # code here
        odd_head=head
        odd=head
        even_head=head.next
        even=head.next
        
        while even and even.next:
            odd.next=even.next
            odd=odd.next 
            even.next=odd.next 
            even=even.next 
            
        odd.next=even_head 
        
        return odd_head