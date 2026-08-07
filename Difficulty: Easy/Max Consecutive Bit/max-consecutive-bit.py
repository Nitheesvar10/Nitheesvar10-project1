class Solution:
    def maxConsecBits(self, arr):
        #code here 
        left=0
        right=0
        max_count=0
        cnt=0
        while right<len(arr):
            cnt+=1
            
            while arr[right]!=arr[left]:
                cnt-=1
                
                left+=1
                
            max_count=max(max_count,right-left+1)
            right+=1
            
            
        return max_count