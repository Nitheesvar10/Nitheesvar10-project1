class Solution:
    def solve(self,idx,subset,total):
        if total >self.Sum:
            return 
        if total==self.Sum:
            if len(subset)==self.lenght:
                self.result.append(subset.copy())
            return 
                
        if idx>=len(self.arr):
            return 
        subset.append(self.arr[idx])
        total+=self.arr[idx]
        self.solve(idx+1,subset,total)
        e=subset.pop()
        total-=e
        self.solve(idx+1,subset,total)
        
        
    def combinationSum(self, n, k):
        # code here
        self.arr=[i for i in range(1,10)]
        self.lenght=k
        self.Sum=n
        self.result=[]
        total=0
        
        self.solve(0,[],total)
        return self.result 