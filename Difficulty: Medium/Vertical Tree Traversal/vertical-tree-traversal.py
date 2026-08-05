''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        nodes=[]
        cnt=0
        
        def dfs(node,row,col):
            nonlocal cnt
            
            if node is None:
                return 
            
            nodes.append([col,row,cnt,node.data])
            
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
            
        dfs(root,0,0)
        
        nodes.sort(key=lambda x:(x[0],x[1],x[2]))
        ans=[]
        prev=float("-inf")
        for col,row,order,val in nodes:
            if prev!=col:
                ans.append([])
                prev=col
            ans[-1].append(val)
            
        return ans 
            
        