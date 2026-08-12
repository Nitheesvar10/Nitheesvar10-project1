class Solution:
    def findFloor(self, arr, x):
        # code here
        left=0
        right=len(arr)-1
        self.floor=None 
        while left <=right:
            mid=left+(right-left)//2
            
            if arr[mid]<=x:
                self.floor=mid 
                left=mid+1
            else:
                right=mid-1
        return self.floor if self.floor  is not None else -1