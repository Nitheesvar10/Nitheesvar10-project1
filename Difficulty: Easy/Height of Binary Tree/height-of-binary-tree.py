''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def solve(self,node):
        
        if node is None:
                return -1 
                
        left=self.solve(node.left)
        right=self.solve(node.right)
        return 1+max(left,right)
    def height(self, root):
     
        return self.solve(root)
        
        