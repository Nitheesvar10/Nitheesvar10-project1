''' Structure of linked list Node
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    #code here
    cur=head
    while cur and cur.next:
        if(cur.data ==cur.next.data):
            cur.next=cur.next.next 
        else:
            cur=cur.next
    
    return head 
        