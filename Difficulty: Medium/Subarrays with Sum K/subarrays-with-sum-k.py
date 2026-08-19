class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        cnt=0
        hash={0:1}
        cur_sum=0
        for i in range(len(arr)):
            cur_sum+=arr[i]
            
            e=cur_sum-k
            
            if e in hash:
                cnt+=hash[e]
                
            hash[cur_sum]=hash.get(cur_sum,0)+1
            
        return cnt 
        