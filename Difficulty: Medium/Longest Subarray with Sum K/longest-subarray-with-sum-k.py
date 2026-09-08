class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        hash={0:-1}
        max_lenght=0
        cur_sum=0
        for i in range(0,len(arr)):
            cur_sum+=arr[i]
            
            e=cur_sum-k
            
            if  e in hash:
                max_lenght=max(max_lenght,i-hash[e])
                
            if cur_sum not in hash:
                hash[cur_sum]=i
            
        return max_lenght
            
    
