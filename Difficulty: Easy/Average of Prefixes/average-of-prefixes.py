class Solution:
    def prefixAvg(self, arr):
        # code here
        
        pre_sum=[0]*len(arr)
        pre_sum[0]=arr[0]
        for i in range(1,len(arr)):
            pre_sum[i]=(arr[i]+pre_sum[i-1])
            
        for i in range(1,len(arr)):
            pre_sum[i]=pre_sum[i]//(i+1)
            
            
            
            
        return pre_sum