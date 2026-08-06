class Solution:
    def leastWeightCapacity(self, arr, D):
        # code here
        low=max(arr)
        high=sum(arr)
        ans=high
        
        while (low<=high):
            cap=low+(high-low)//2
            
            if self.shipcap(arr,D,cap):
                ans=cap
                high=cap-1
            else:
                low=cap+1
        return ans 
                
                
        
    def shipcap(self,arr,D,cap):
        day=1
        cur_cap=0
        for i in arr:
            if cur_cap+i>cap:
                day=day+1
                cur_cap=i
            else:
                cur_cap+=i
        return day<=D
            
            
            