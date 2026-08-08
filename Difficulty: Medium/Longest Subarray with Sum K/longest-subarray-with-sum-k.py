class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        cur_sum=0
        max_len=0
        hash={0:-1}
        for i in range(len(arr)):
            cur_sum+=arr[i]
            
            e=cur_sum-k
            
            if e in hash:
                max_len=max(max_len,i-hash[e])
                
            if cur_sum not in hash:
                hash[cur_sum]=i
                
        return max_len