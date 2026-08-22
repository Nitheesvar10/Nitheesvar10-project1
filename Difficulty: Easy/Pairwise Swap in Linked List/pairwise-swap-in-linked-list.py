''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        # code here
        arr=[]
        cur=head
        while cur:
            arr.append(cur.data)
            cur=cur.next
        
        for i in range(0,len(arr)-1,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            
        cur=head
        index=0
        while cur:
            cur.data=arr[index]
            index+=1
            cur=cur.next
            
        return head 
        
            