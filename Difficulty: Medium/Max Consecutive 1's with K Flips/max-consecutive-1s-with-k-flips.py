class Solution:
    def maxOnes(self, arr, k):
        # code here
        left=0
        right=0
        
        zero_cnt=0
        
        max_cnt=0
        
        while right <len(arr):
            if arr[right]==0:
                zero_cnt+=1
                
            while zero_cnt >k:
                if arr[left]==0:
                    zero_cnt-=1
                    
                left+=1
                
                
            max_cnt=max(right-left+1,max_cnt)
            
            
            right+=1
        
        return max_cnt 
        