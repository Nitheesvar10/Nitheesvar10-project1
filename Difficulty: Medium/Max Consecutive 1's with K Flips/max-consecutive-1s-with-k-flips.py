class Solution:
    def maxOnes(self, arr, k):
        # code here
        left=0
        right=0
        cnt=0
        max_cnt=0
        cnt_0=0
        
        while right<len(arr):
            if arr[right]==0:
                
                cnt_0+=1
            
            while cnt_0 >k:
                if arr[left]==0:
                    cnt_0-=1
                left+=1
            
            if cnt_0<=k:
                max_cnt=max(max_cnt,right-left+1)
                
                
            
            right+=1
            
        return max_cnt