class Solution:
    def countSubarray(self, arr, k):
        # code here
        if k<=1:
            return 0
        left=0
        right=0
        cnt=0
        cur_prod=1
        
        while right <len(arr):
            cur_prod*=arr[right]
            
            
            while cur_prod >=k:
                cur_prod/=arr[left]
                left+=1
            if cur_prod <k:
                
                cnt+=right-left+1
            
            
            right+=1
            
            
        return cnt
                
                