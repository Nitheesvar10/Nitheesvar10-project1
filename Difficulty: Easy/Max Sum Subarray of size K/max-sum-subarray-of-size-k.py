class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        left=0
        right=0
        max_sum=0
        cur_sum=0
        
        while  right <len(arr):
            cur_sum+=arr[right]
            
            while right -left+1>k:
                cur_sum-=arr[left]
                
                left+=1
                
            max_sum=max(cur_sum,max_sum)
            
            right+=1
        
        return max_sum 
            