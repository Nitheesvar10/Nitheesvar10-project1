class Solution:

	
	def search(self,pat, txt):
	    # code here
	    h1={}
	    h2={}
	    count=0
	    
	    for i in range(len(pat)):
	        h1[pat[i]]=h1.get(pat[i],0)+1
	        
	    left=0
	    right=0
	    
	    while right <len(txt):
	        h2[txt[right]]=h2.get(txt[right],0)+1
	        
	        while right-left+1 >len(pat):
	            h2[txt[left]]-=1
	            if h2[txt[left]]==0:
	                del h2[txt[left]]
	            
	            left+=1
	            
	        if h1==h2:
	            count+=1
	            
	        right+=1
	       
	            
	    return count 