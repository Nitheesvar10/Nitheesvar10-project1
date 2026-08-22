'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        # code here
        arr=[]
        cur=head
        while cur:
            arr.append(cur.data)
            cur=cur.next
        
        k=k%len(arr)
        for i in range(0,k):
            arr.append(arr.pop(0))
            
            
            
            
        cur=head
        ind=0
        while cur:
            cur.data=arr[ind]
            ind+=1
            cur=cur.next
            
        return head
        
        
        