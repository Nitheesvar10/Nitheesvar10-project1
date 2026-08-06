class Solution:
    def findFloor(self, arr, x):
        # code here
        low=0
        high=len(arr)-1
        self.floor=None
        
        
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]<=x:
                self.floor=mid
                low=mid+1
                
            else:
                high=mid-1
                
        return self.floor if self.floor is not None else -1