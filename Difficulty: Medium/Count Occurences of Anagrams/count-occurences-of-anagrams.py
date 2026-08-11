class Solution:
	def search(self,pat, txt):
	    # code here\
	    count=0
	    f1={}
	    for i in pat:
	        f1[i]=f1.get(i,0)+1
	        
	    f2={}
	    
	    left=0 
	    right=0
	    
	    while right <len(txt):
	        f2[txt[right]]=f2.get(txt[right],0)+1
	        
	        while right-left+1>len(pat):
	            f2[txt[left]]-=1
	            
	            if f2[txt[left]]==0:
	                del f2[txt[left]]
	                
	            left+=1
	            
	           
	        if right-left+1==len(pat):
	            if f1==f2:
	                count+=1
	               

	        
	        right+=1
	        
	    return count    
	   
	        