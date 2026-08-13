class Solution:  
    def solve(self,idx,arr,dp):
        if idx==0:
            return arr[0]
            
        if idx==1:
            return max(arr[0],arr[1])
            
        if dp[idx]!=-1:
            return dp[idx]
            
        pick=arr[idx]+self.solve(idx-2,arr,dp)
        notpick=0+self.solve(idx-1,arr,dp)
        dp[idx]= max(notpick,pick)
        return dp[idx]
        
    def findMaxSum(self, arr):
        
        dp=[-1]*len(arr)
        # code here
        return self.solve(len(arr)-1,arr,dp)
        