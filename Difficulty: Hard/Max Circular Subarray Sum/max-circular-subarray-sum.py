class Solution:
    def maxCircularSum(self, arr):
        # code here
        globmax,globmin=arr[0],arr[0]
        cur_max,cur_min=0,0
        total=0
        for i in arr:
            cur_max=max(cur_max+i,i)
            cur_min=min(i,cur_min+i)
            total+=i
            globmax=max(cur_max,globmax)
            globmin=min(cur_min,globmin)
            
        return max(globmax,total-globmin) if globmax>0 else globmax