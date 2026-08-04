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
        self.solve(node.right)
        self.result.append(node.data)
    def postOrder(self, root):
        self.result=[]
        self.solve(root)
        return self.result 

        
        