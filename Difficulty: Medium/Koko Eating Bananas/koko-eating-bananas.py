class Solution:
    def kokoEat(self, arr, k):
        # Code here
        low=1
        high=max(arr)
        while low<=high:
            speed=low+(high-low)//2
            
            if self.complete(arr,k,speed):
                ans=speed
                high=speed-1
            else:
                low=speed+1
                
        return ans 
        
    def complete(self,arr,k,speed):
        s=0
        for i in arr:
            s+=(i+speed-1)//speed
            
        return s<=k