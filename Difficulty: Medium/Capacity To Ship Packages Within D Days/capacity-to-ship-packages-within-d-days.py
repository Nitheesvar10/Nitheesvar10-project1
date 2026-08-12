class Solution:
    def leastWeightCapacity(self, arr, D):
        # code here
        low=max(arr)
        high=sum(arr)
        ans=None 
        
        while low<=high:
            mid=low+(high-low)//2
            
            if self.go(arr,mid,D):
                ans=mid
                high=mid-1 
                
            else:
                low=mid+1
        return ans 
        
    def go(self,arr,w,D):
        weight=0
        d=1
        for i in arr:
            
            if (weight+i)<=w:
                weight+=i
                
            else:
                weight=i
                d+=1
        
        return d<=D
            
            