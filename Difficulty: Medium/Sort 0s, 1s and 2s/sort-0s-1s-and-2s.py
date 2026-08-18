class Solution:
    def sort012(self, arr):
        # code here
        left=0
        mid=0
        right=len(arr)-1
        while right >=mid:
            if arr[mid]==0:
                arr[mid],arr[left]=arr[left],arr[mid]
                mid+=1
                left+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[right]=arr[right],arr[mid]
                right-=1
            
        return arr