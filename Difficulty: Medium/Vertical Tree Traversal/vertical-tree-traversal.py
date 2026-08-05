''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
# from colllections import deque
class Solution:
    
    def dfs(self,node,row,col):
        if node is None:
            return 
        
        self.nodes.append([col,row,self.cnt,node.data])
        self.cnt+=1
        
        
        self.dfs(node.left,row+1,col-1)
        self.dfs(node.right,row+1,col+1)
        
    def verticalOrder(self, root): 
        # code here

        self.cnt=0
        self.nodes=[]
        self.dfs(root,0,0)
        self.nodes.sort(key=lambda x:(x[0],x[1],x[2]))
        ans=[]
        prev=float("-inf")
        
        for col,row,order,val in self.nodes:
            if prev!=col:
                ans.append([])
                prev=col
                
            ans[-1].append(val)
            
        return ans 
        
        