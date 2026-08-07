class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        if k*m >len(arr):
            return -1
            
        low=min(arr)
        high=max(arr)
        ans=high
        
        while (low<=high):
            day=low+(high-low)//2
            
            if self.bloom(arr,k,m,day):
                ans=day 
                high=day-1
                
            else:
                low=day+1
                
        return ans 
        
    def bloom(self,arr,k,m,day):
        b=0
        count=0
        for i in arr:
            if i<=day:
                count+=1
                if count==k:
                    b+=1
                    count=0
            else:
                count=0
        return b>=m