class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        low=1
        ans=None
        high=arr[len(arr)-1]-arr[0]
        while low <=high:
            mid=low+(high-low)//2
            
            if self.spot(arr,mid,k):
                ans=mid
                low=mid+1
                
            else:
                high=mid-1
                
        return ans 
    
    def spot(self,arr,mid,k):
        last=arr[0]
        count=1
        for i in range(1,len(arr)):
            if arr[i]-last>=mid:
                count+=1
                last=arr[i]
                
        return  count>=k
                
        