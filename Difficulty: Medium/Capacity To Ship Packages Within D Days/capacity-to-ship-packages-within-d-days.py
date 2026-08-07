class Solution:
    def leastWeightCapacity(self, arr, D):
        # code here
        low=max(arr)
        high=sum(arr)
        ans=high
        while low<=high:
            cap=low+(high-low)//2
            
            if self.capable(arr,D,cap):
                ans=cap
                high=cap-1
                
            else:
                low=cap+1
        return ans 
    
    def capable(self,arr,D,cap):
        d=1
        c=0
        for i in arr:
            if c+i>cap:
                d+=1
                c=i
            else:
                c+=i
        return d<=D
        
                
            
            
            