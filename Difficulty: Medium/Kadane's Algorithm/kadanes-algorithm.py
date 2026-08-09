class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        cur_sum=0
        max_sum=arr[0]
        for i in range(len(arr)):
            cur_sum+=arr[i]
            
            max_sum=max(max_sum,cur_sum)
            
            if cur_sum<0:
                cur_sum=0
                # continue 
            
        return max_sum