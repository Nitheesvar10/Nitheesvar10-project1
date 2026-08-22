'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        dummy=Node(0)
        cur=dummy
        while head1 and head2:
            if (head1.data <head2.data):
                cur.next=head1
                head1=head1.next 
                cur=cur.next
            else:
                cur.next=head2
                head2=head2.next 
                cur=cur.next 
                
        if head1:
            cur.next=head1
        
        else:
            cur.next=head2 
            
        
        return dummy.next
                