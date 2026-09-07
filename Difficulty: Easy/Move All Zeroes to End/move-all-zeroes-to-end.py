class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	left=0
    	for i in range(0,len(arr)):
    	    if arr[i]!=0:
    	        arr[i],arr[left]=arr[left],arr[i]
    	        left+=1
    	        
        return arr