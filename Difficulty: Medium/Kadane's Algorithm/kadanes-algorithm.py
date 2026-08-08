class Solution:
    def maxSubarraySum(self, arr):
        # Code here]
        max_sum=arr[0]
        cur_sum=0
        for i in arr:
            cur_sum+=i
            max_sum=max(max_sum,cur_sum)
            if cur_sum<0:
                cur_sum=0
                continue
            
            max_sum=max(max_sum,cur_sum)
            
        return  max_sum