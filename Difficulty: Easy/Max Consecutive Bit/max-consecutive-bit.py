class Solution:
    def maxConsecBits(self, arr):
        #code here 
        left=0
        right=0
        cnt=0
        max_cnt=0
        while right <len(arr):
            
            cnt-=1
            
            while arr[left]!=arr[right]:
                cnt-=1
                left+=1
                
            max_cnt=max(max_cnt,right-left+1)
            
            right+=1
        return max_cnt 