class Solution:
    def productExceptSelf(self, arr):
        # code here
        pre_prod=[0]*len(arr)
        suf_prod=[0]*len(arr)
        
        pre_prod[0]=arr[0]
        suf_prod[-1]=arr[-1]
        
        for i in range(1,len(arr)):
            pre_prod[i]=arr[i]*pre_prod[i-1]
            
        for i in range(len(arr)-2,-1,-1):
            suf_prod[i]=arr[i]*suf_prod[i+1]
            
        for i in range (0, len(arr)):
            if i ==0:
                arr[0]=suf_prod[1]
            elif i==len(arr)-1:
                arr[i]=pre_prod[-2]
                
            else:
                arr[i]=pre_prod[i-1]*suf_prod[i+1]
                
        return arr
                