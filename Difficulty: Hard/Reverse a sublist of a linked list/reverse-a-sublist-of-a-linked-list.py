''' Structure of a Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

'''
class Solution:
    def reverseBetween(self, a, b, head):
        # code here
        if a==b:
            return head
            
        dummy =Node(0)
        dummy.next=head
        prevleft=dummy 
        
        for _ in range(a-1):
            prevleft=prevleft.next
        
        h=prevleft.next
            
        cur=prevleft.next 
        prev=None 
        
        for _ in range(b-a+1):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt 
        prevleft.next=prev
        h.next=cur 
    
        return dummy.next 
        
        
            
        
            