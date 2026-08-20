class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        left=0
        right=0
        hash={}
        cnt=0
        max_count=0
        while right<len(s):
            hash[s[right]]=hash.get(s[right],0)+1
            cnt+=1
            
            while hash[s[right]]==2:
                hash[s[left]]-=1
                if hash[s[left]]==0:
                    del hash[s[left]]
                
                left+=1
                
            max_count=max(max_count,right-left+1)
            
            right+=1
            
        return max_count
        
                
            
            
            
            
            