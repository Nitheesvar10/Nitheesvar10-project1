class Solution:
    def findCeil(self, arr, x):
        # code here
        left=0
        self.ceil=None
        right=len(arr)-1
        while (left<=right):
            mid=left+(right-left)//2
            
            if arr[mid]>=x:
                self.ceil=mid
                right=mid-1
                
            else:
                left=mid+1
                
        return self.ceil if self.ceil is not None else -1