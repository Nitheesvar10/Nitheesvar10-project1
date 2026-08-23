class Solution:
    def solve(self,arr,idx,k):
        if k<0:
            return 
        if k==0:
            return True 
            
        if idx>=len(arr):
            return 
        left=self.solve(arr,idx+1,k-arr[idx])
        if left:
            return True 
        right=self.solve(arr,idx+1,k)
        return right 
        
        
    def checkSubsequenceSum(self, arr, k):
        # code here
        return self.solve(arr,0,k)