class Solution:
    def productExceptSelf(self, arr):
        # code here
        prefix=[0]*len(arr)
        suffix=[0]*len(arr)
        
        prefix[0]=arr[0]
        suffix[-1]=arr[-1]
        
        for i in range(1,len(arr)):
            prefix[i]=arr[i]*prefix[i-1]
            
        for i in range(len(arr)-2,-1,-1):
            suffix[i]=arr[i]*suffix[i+1]
            
        result=[0]*len(arr)
        for i in range(0,len(arr)):
            if i==0:
                result[i]=suffix[i+1]
            elif i==len(arr)-1:
                result[i]=prefix[i-1]
                
            else:
                
                result[i]=prefix[i-1]*suffix[i+1]
                
        return result