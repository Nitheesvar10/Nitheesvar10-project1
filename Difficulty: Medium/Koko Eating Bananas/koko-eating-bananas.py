class Solution:
    def kokoEat(self, arr, k):
        # Code here
        low=1
        high=max(arr)
        ans=None 
        while low <=high :
            mid=low+(high-low)//2
            
            if self.caneat(arr,mid,k):
                ans=mid
                high=mid-1 
            else:
                low=mid+1
                
            
                
        return ans 
    
    
    def caneat(self,arr,speed,k):
        hrs=0
        for i in arr:
            hrs+=(i+speed-1)//speed
            
        return hrs<=k
        