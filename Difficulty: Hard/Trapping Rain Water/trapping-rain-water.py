class Solution:
    def maxWater(self, arr):
        # code here
        left=0
        right=len(arr)-1
        left_max=arr[left]
        right_max=arr[right]
        water=0
        while left<right:
            if left_max <right_max:
                left+=1
                left_max=max(left_max,arr[left])
                water+=left_max-arr[left]
                
            else:
                right-=1
                right_max=max(arr[right],right_max)
                water+=right_max-arr[right]
                
                
        return water 
            