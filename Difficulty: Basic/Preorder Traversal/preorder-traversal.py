'''
Structure of Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def solve(self,node):
        if node is None:
            return 
        self.result.append(node.data)
        self.solve(node.left)
        self.solve(node.right)
        
        
    def preOrder(self, root):
        
    # code here
        self.result=[]
        self.solve(root)
        return self.result 