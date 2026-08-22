'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        # Code here
        found=False
        cur=head
        while cur is not None:
            if cur.data==key:
                found=True 
                break
            cur=cur.next 
        
        return found