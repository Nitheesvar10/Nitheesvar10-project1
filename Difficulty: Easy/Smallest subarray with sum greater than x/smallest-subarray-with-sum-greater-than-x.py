class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        left=0
        right=0
        
        cur_sum=0
        min_cnt=float("inf")
        while right <len(arr):
            cur_sum+=arr[right]
            
            while cur_sum>x:
                if cur_sum>x:
                    min_cnt=min(min_cnt,right-left+1)
                cur_sum-=arr[left]
                left+=1
                
            
                
            right+=1
        return min_cnt if min_cnt!=float("inf") else 0
                