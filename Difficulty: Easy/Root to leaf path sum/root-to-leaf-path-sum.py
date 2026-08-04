'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # code here
        if root is None:
            return 
        if root.left is None and root.right is None:
            return target==root.data
        
        return self.hasPathSum(root.left,target-root.data) or self.hasPathSum(root.right,target-root.data)