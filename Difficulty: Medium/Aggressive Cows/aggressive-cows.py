class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        
        low=1
        high=arr[len(arr)-1]-arr[0]
        
        while low<=high:
            pos=low+(high-low)//2
            
            if self.proper(arr,k,pos):
                ans=pos
                low=pos+1
            else:
                high=pos-1
                
        return ans 
        
    def proper(self,arr,k,pos):
        count=1
        last_pos=arr[0]
        
        for i in range (1,len(arr)):
            if arr[i]-last_pos >=pos:
                count+=1
                last_pos=arr[i]
                
        return  count>=k