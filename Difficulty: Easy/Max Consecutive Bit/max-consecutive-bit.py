class Solution:
    def maxConsecBits(self, arr):
        #code here 
        left=0
        right=0
        max_cnt=0
        while right <len(arr):
            
            while arr[right]!=arr[left]:
                left+=1
                
            max_cnt=max(max_cnt,right-left+1)
            
            right+=1
            
        return max_cnt
                
            