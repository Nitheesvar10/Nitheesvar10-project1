class Solution:
    def maxWater(self, arr):
        # code here
        left=0
        right=len(arr)-1
        
        water=0
        left_max=arr[left]
        right_max=arr[right]
        
        while left<right :
            if arr[left]<arr[right]:
                left+=1
                left_max=max(left_max,arr[left])
                water+=left_max-arr[left]
            else:
                right-=1
                right_max=max(right_max,arr[right])
                water+=right_max-arr[right]
                
        return water 