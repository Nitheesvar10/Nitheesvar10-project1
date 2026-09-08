class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        left=0
        right=0
        h={}
        max_len=0
        while right <len(s):
            h[s[right]]=h.get(s[right],0)+1
            
            
            while h[s[right]]==2:
                h[s[left]]-=1
                if h[s[left]]==0:
                    del h[s[left]]
                    
                
                
                left+=1
                
            max_len=max(max_len,right-left+1)
            
            
            right+=1
            
        return max_len 
                
            
                
                
            
            
            
            
            