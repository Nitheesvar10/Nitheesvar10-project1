class Solution:
    def solve(self,arr,idx):
        if idx>=self.n:
            self.result.append("".join(arr))
            return 
        arr[idx]="0"
        self.solve(arr,idx+1)
        arr[idx]="1"
        self.solve(arr,idx+1)
        

    
    def binstr(self, n):
        # code here
        self.n=n
        self.result=[]
        arr=["0"]*n
        
        self.solve(arr,0)
        
        return self.result 
        