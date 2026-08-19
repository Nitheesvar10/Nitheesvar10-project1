class Solution:
    def totalElements(self, arr):
        # Code here
        dict={}
        left=0
        right=0
        max_cnt=0
        while right <len(arr):
            dict[arr[right]]=dict.get(arr[right],0)+1
            
            while len(dict)>2:
                
                dict[arr[left]]-=1
                if dict[arr[left]]==0:
                    del dict[arr[left]]
                left+=1
                
            max_cnt=max(max_cnt,right-left+1)
            
            right+=1
        return max_cnt
            
                