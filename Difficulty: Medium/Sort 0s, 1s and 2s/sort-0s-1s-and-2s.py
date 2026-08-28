class Solution:
    def sort012(self, arr):
        # code here
        left=0
        right=len(arr)-1
        mid=0
        while mid <=right:
            if arr[mid]==0:
                arr[left],arr[mid]=arr[mid],arr[left]
                
                left+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
                
            else:
                arr[right],arr[mid]=arr[mid],arr[right]
                right-=1
                
        return arr