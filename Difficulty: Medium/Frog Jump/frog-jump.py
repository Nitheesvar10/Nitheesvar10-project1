class Solution:
    def minCost(self, height: list[int]) -> int:
        # code here
        def solve(idx,dp):
            if idx==0:
                return 0
            
            if idx==1:
                return abs(height[idx]-height[idx-1])
            
            if dp[idx]!=-1:
                return dp[idx]
                
                
            jump1=solve(idx-1,dp)+abs(height[idx]-height[idx-1])
            
            if idx>1:
                jump2=solve(idx-2,dp)+abs(height[idx]-height[idx-2])
                
            else:
                jump2=float("inf")
                
            dp[idx]= min(jump1,jump2)
            return dp[idx]
            
            
        dp=[-1]*len(height)
            
        return solve(len(height)-1,dp)