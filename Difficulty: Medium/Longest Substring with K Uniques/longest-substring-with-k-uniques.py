class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        if k>len(s):
            return -1
        hash={}
        left=0
        right=0
        cnt=0
        max_count=-1
        
        while right <len(s):
            hash[s[right]]=hash.get(s[right],0)+1
            cnt+=1
            
            
            while len(hash)>k:
                hash[s[left]]-=1
                if hash[s[left]]==0:
                    del hash[s[left]]
                left+=1
                
            if len(hash)==k:   
                max_count=max(max_count,right-left+1)
            
            right+=1
        return max_count
            
        
        