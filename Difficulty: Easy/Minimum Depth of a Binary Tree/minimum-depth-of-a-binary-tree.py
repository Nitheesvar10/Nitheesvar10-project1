'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def solve(self,node):
        if node is None:
            return 0
        
        if node.left is None:
            return 1+self.solve(node.right)
        if node.right is None:
            return 1+self.solve(node.left)
            
        left=self.solve(node.left)
        right=self.solve(node.right)
        return 1+min(left,right)
        
            
        
    def minDepth(self, root):
        #Code here
        
        return self.solve(root)
        