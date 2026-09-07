class Solution:
    def findEquilibrium(self, arr):
        # code here

        pre_sum=[0]*len(arr)
        suf_sum=[0]*len(arr)
        
        pre_sum[0]=arr[0]
        suf_sum[-1]=arr[-1]
        
        for i in range(1,len(arr)):
            pre_sum[i]=arr[i]+pre_sum[i-1]
            
        for i in range(len(arr)-2,-1,-1):
            suf_sum[i]=arr[i]+suf_sum[i+1]
            
            
            
        for i in range(0,len(arr)):
            if pre_sum[i]==suf_sum[i]:
                return i 
                
        return -1 