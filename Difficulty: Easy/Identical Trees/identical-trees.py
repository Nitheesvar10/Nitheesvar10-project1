'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def solve(self,node,result):
        if node is None:
            return None
        result.append(node.data)
        self.solve(node.left,result)
        self.solve(node.right,result)
    
    def isIdentical(self, r1, r2):
        # code here
        self.result1=[]
        self.result2=[]
        self.solve(r1,self.result1)
        self.solve(r2,self.result2)
        if self.result1==self.result2:
            return True 
        else:
            return False 
            
        
        
        