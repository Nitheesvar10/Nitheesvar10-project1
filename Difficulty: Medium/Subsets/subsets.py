class Solution:
    def solve(self,arr,idx,subset):
        
        if idx==len(arr):
            self.result.append(subset.copy())
            return 
        
        subset.append(arr[idx])
        self.solve(arr,idx+1,subset)
        subset.pop()
        self.solve(arr,idx+1,subset)
        
    def subsets(self, arr):
        self.lenght=len(arr)
        self.result=[]
        self.solve(arr,0,[])
        
        return self.result
        