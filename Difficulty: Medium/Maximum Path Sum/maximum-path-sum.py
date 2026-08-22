''' Structure of binary tree node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def solve(self,node):
        if node is None:
            return 0
            
        leftsum=self.solve(node.left)
        if leftsum<0:
            leftsum=0
            
        right_sum=self.solve(node.right)
        if right_sum<0:
            right_sum=0
            
        self.maxi=max(leftsum+right_sum+node.data,self.maxi)
        return node.data+max(leftsum,right_sum)
        
    def findMaxSum(self, root): 
        # code here
        self.maxi=float("-inf")
        self.solve(root)
        return self.maxi
        
        
        
        
        