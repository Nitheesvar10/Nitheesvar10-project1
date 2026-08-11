class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        left=0
        right=0
        count=0
        f={}
        while  right<len(s):
            f[s[right]]=f.get(s[right],0)+1
            
            while f[s[right]]>=2:
                f[s[left]]-=1
                
                left+=1
                
            count=max(count,right-left+1)
            
            right+=1
            
        return count
                
            