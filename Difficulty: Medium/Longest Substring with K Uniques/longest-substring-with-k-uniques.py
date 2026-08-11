class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        count=-1
        left=0
        right=0
        f={}
        while right <len(s):
            f[s[right]]=f.get(s[right],0)+1
            
            while len(f)>k:
                f[s[left]]-=1
                if f[s[left]]==0:
                    del f[s[left]]
                left+=1
                
            if len(f)==k:
                
                count=max(count,right-left+1)
            
            right+=1
            
            
        return count