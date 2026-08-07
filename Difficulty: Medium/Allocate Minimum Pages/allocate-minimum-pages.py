class Solution:
    def findPages(self, arr, k):
        # code here
        if k>len(arr):
            return -1
            
        low=max(arr)
        
        high=sum(arr)
        
        while low <=high:
            
            pages=low+(high-low)//2
            
            if self.ok(arr,k,pages):
                ans=pages
                high=pages-1
                
            else:
                low=pages+1
                
        return ans  
    def ok(self,arr,k,pages):
        count=1
        cur_count=0
        for i in range(len(arr)):
            if cur_count+arr[i]>pages:
                count+=1
                cur_count=arr[i]
            else:
                cur_count+=arr[i]
                
        return  count<=k