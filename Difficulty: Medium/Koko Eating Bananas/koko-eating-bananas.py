class Solution:
    def kokoEat(self, arr, k):
        # Code here
        low=1
        high=max(arr)
        ans=high
        
        while (low<=high):
            mid=low+(high-low)//2
            
            if self.canEat(arr,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
                
        return ans 
        
    def canEat(self,arr,k,mid):
        hours=0
        for b in arr:
            hours+=(b+mid-1)//mid
        
        return hours<=k
            