class Solution:
    def findEquilibrium(self, arr):
        # code here
        pre_sum=[0]*len(arr)
        suf_sum=[0]*len(arr)
        pre_sum[0]=arr[0]
        
        for i in range(1,len(arr)):
            pre_sum[i]=pre_sum[i-1]+arr[i]
            
        suf_sum[len(arr)-1]=arr[len(arr)-1]
        
        for i in range(len(arr)-2,-1,-1):
            suf_sum[i]=suf_sum[i+1]+arr[i]
            
        for i in range(len(arr)):
            if pre_sum[i]==suf_sum[i]:
                return i 
        
        return -1
