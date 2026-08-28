class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	left=0
    	right=0
    	while right <len(arr):
    	    
    	    if arr[right]!=0:
    	        arr[right],arr[left]=arr[left],arr[right]
    	        
    	        left+=1
            right+=1
        return arr
        