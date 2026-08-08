class Solution:
	def maxProduct(self,arr):
		# code here
		left_prod=1
		right_prod=1
		
		max_prod=float("-inf")
		
		for i in range(len(arr)):
		    if left_prod==0:
		        left_prod=1
		    if right_prod==0:
		        right_prod=1
		        
		    left_prod*=arr[i]
		    right_prod*=arr[len(arr)-i-1]
		    
		    max_prod=max(max_prod,right_prod,left_prod)
		    
        return max_prod