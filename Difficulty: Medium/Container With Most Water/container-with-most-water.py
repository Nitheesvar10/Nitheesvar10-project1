class Solution:
    def maxWater(self, arr):
        # code here
        left=0
        right=len(arr)-1
        max_area=float("-inf")
        while left < right :
            width=right-left

            lenght=min(arr[left],arr[right])
            
            max_area=max(max_area,(width*lenght))
            
            if arr[left]<arr[right]:
                left+=1
                
            else:
                right-=1
                
        return max_area  if max_area!= float("-inf") else 0
        
        
                
            
            