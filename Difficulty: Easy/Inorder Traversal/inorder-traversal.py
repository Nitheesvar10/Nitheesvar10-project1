''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def solve(self,node):
        if node is None:
            return 
        self.solve(node.left)
        self.result.append(node.data)
        self.solve(node.right)
        
        
    def inOrder(self, root):
        self.result=[]
        self.solve(root)
        return self.result 
        # code here
        