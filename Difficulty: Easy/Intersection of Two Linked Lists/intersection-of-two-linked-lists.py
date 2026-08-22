# structure of list node:
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None

class Solution:
    def findIntersection(self, head1, head2):
        # code here
        s=set()
        cur=head2
        while cur:
            s.add(cur.data)
            cur=cur.next 
            
        dummy=Node(0)
        tmp=dummy
        cur=head1
        while cur :
            if cur.data in s:
                dummy.next=Node(cur.data)
                dummy=dummy.next 
            cur=cur.next 
                
        return tmp.next
            