class Solution:
    def maxWater(self, arr):
        # code here
        left=0
        right=len(arr)-1
        max_water=0
        while left<right :
            b=right-left
            lenght=min(arr[left],arr[right])
            max_water=max(max_water ,(b*lenght))
            
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
                
        return max_water 