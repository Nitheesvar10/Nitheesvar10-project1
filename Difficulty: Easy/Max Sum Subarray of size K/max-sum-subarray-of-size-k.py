class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        left=0
        
        right=0
        cur_sum=0
        max_sum=float("-inf")
        
        while right<len(arr):
            cur_sum+=arr[right]
            
            while right-left+1>k:
                cur_sum-=arr[left]
                left+=1
            
            if right-left+1==k:
                max_sum=max(max_sum,cur_sum)
            right+=1
            
        return max_sum
            
            
        