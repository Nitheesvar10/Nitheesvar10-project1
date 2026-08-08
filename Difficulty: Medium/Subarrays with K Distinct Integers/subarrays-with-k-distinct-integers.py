class Solution:
    def exactlyK(self, arr, k):
        # Code here
        def atmost(k):
            dict={}
            left=0
            right=0
            count=0
            
            while right<len(arr):
                dict[arr[right]]=dict.get(arr[right],0)+1
                
                while len(dict)>k:
                    dict[arr[left]]-=1
                    if dict[arr[left]]==0:
                        del dict[arr[left]]
                        
                    left+=1
                    
                if len(dict)<=k:
                    count+=right-left+1
                    
                right+=1
                
                
            return count
            
        return atmost(k)-atmost(k-1)
        