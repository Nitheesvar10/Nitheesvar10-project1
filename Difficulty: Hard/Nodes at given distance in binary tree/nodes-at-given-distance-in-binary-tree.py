'''
Structure of Binary Tree Node
 class Node:
     def __init__(self, val):
         self.data = val
        self.left = None
        self.right = None
'''

from collections import deque 
class Solution:
    def kDistanceNodes(self, root, target, k):
        # code here
        parent={}
        q=deque([root])
        targetNode=None
        while q:
            node=q.popleft()
            
            if node.data ==target:
                targetNode=node
            if node.left:
                parent[node.left]=node
                q.append(node.left)
            if node.right:
                parent[node.right]=node
                q.append(node.right)
        
                
        q=deque([targetNode])
        visited={targetNode}
        distance=0
        
        while q:
            if distance==k:
                break
            for _ in range(len(q)):
                node=q.popleft()
                
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])
                
            distance+=1
        
        result=[]
        
        for _ in range(len(q)):
            result.append(q.popleft().data)
            
        result.sort()
        return result 
        
        