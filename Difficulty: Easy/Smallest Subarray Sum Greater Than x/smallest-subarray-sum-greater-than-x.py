class Solution:
    def smallestSubWithSum(self, x, arr):
        # code here 
    
        left=0
        right=0
        cur_sum=0
        max_len=float("inf")
        while right<len(arr):
            cur_sum+=arr[right]
            
            while cur_sum >x:
                max_len=min(max_len,right-left+1)
                cur_sum-=arr[left]
                
                left+=1
                
            right+=1
            
        return max_len if max_len!=float("inf") else 0
            
            
                
            
        
