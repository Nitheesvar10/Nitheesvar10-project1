class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        if k*m > len(arr):
            return -1 
        ans=-1
        low=min(arr)
        high=max(arr)
        while low<=high:
            mid=low+(high-low)//2
            
            if self.make(arr,k,m,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 
        
    def make(self,arr,k,m,mid):
        b=0
        count=0
        for i in arr:
            if i<=mid:
                count+=1
                if count==k:
                    b+=1
                    count=0
                    
            else:
                count =0
        return b>=m