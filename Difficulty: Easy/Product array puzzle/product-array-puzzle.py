class Solution:
    def productExceptSelf(self, arr):
        # code here
        prefix_prod=[0]*len(arr)
        
        prefix_prod[0]=arr[0]
        
        suffix_prod=[0]*len(arr)
        
        suffix_prod[len(arr)-1]=arr[len(arr)-1]
        
        for i in range(1,len(arr)):
            prefix_prod[i]=prefix_prod[i-1]*arr[i]
        for i in range(len(arr)-2,-1,-1):
            suffix_prod[i]=suffix_prod[i+1]*arr[i]
            
            
        result=[0]*len(arr)
        for i in range(len(arr)):
            if i==0:
                result[i]=suffix_prod[i+1]
            elif i==len(arr)-1:
                result[i]=prefix_prod[i-1]
            else:
                result[i]=prefix_prod[i-1]*suffix_prod[i+1]
            
        return result
    