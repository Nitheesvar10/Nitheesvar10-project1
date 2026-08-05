'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def leafnode(self,node):
        if node.left is None and node.right is None:
            return True
        return False
        
    def left(self,node):
        if node is None:
            return 
        if not (self.leafnode(node)):
            self.result.append(node.data)
        if node.left:
            self.left(node.left)
            
        else:
            self.left(node.right)
        
    def leaf(self,node):
        if not node:
            return 
            
        if self.leafnode(node):
            self.result.append(node.data)
            
        self.leaf(node.left)
        self.leaf(node.right)
        
        
    def right(self,node):
        if node is None:
            return 
        
        
        if node.right:
            self.right(node.right)
        else:
            self.right(node.left)
            
        if not(self.leafnode(node)):
            self.result.append(node.data)
            
        
    
        
        
            
            
    def boundaryTraversal(self, root):
        if root.left is None and root.right is None:
            return [root.data]
        # code here
        self.result = [root.data]

        self.left(root.left)
        self.leaf(root)
        self.right(root.right)
        
        return self.result 
                
        
               
        