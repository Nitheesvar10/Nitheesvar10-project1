class Solution:
    def countSubarray(self, arr, k):
        # code here
        if k<=1:
            return 0 
            
        left=0
        right=0
        cur_prod=1
        count=0
        while right<len(arr):
            cur_prod*=arr[right]
            
            while cur_prod >=k:
                cur_prod=cur_prod//arr[left]
                
                left+=1
            
            count+=right-left+1
            
            right+=1
        
        return count 
                