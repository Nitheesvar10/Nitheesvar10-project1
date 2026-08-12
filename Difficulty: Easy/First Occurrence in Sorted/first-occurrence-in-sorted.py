class Solution:
    def firstSearch(self, arr, k):
        # Code Here
        left=0
        right=len(arr)-1
        ans=None
        while left<=right:
            mid=left+(right-left)//2
            
            if arr[mid]==k:
                ans=mid
                right=mid-1 
                
            elif arr[mid]>k:
                right=mid-1
                
            else:
                left=mid+1
                
        return ans if ans  is not None else -1