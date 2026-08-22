''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if head is None:
            return 
        
        if x==1:
            temp=head 
            head=head.next 
            temp.next=None
            del temp 
            return head
            
        count=0
        prev=None
        cur=head 
        
        while count<x-1:
            prev=cur 
            cur=cur.next 
            count+=1
            
        prev.next=cur.next 
        
        return  head 
        
