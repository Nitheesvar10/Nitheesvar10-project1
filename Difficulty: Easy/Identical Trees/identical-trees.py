'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''


class Solution:
    def dfs(self,node,result):
        if node is None:
            return None
            
            
        self.dfs(node.left,result)
        self.dfs(node.right,result)
        result.append(node.data)
        
    def isIdentical(self, r1, r2):
        # code here
        
        result1=[]
        result2=[]
        
        self.dfs(r1,result1)
        self.dfs(r2,result2)
        
        if result1==result2:
            return True  
        else:
            return False
        