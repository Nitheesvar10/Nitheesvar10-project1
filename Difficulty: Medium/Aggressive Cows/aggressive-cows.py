class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        low=1
        high=arr[len(arr)-1]-arr[0]
        
        while low<=high:
            spot=low+(high-low)//2
            
            if self.spotted(arr,k,spot):
                ans=spot
                low=spot+1
            else:
                high=spot-1
                
        return ans
        
    def spotted(self,arr,k,spot):
        count=1
        last=arr[0]
        for i in range(1,len(arr)):
            if arr[i]-last>=spot:
                count+=1
                last=arr[i]
                
        return count>=k