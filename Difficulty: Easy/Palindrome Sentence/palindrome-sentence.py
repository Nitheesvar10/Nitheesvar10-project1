class Solution:
	def isPalinSent(self, s):
		# code here
		left=0
		right=len(s)-1
		while left<=right:
		    if not s[left].isalnum():
		        left+=1
		        continue
		        
		    if not s[right].isalnum():
		        right-=1
		        continue 
		    if s[left].lower() != s[right].lower():
		        return False 
		        
		    
		    left+=1
		    right-=1
		    
	    return True 