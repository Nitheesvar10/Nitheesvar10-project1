class Solution:
    def solve(self,arr,idx):
        if idx==len(arr):
            self.result.append("".join(arr.copy()))
            return 
        arr[idx]="0"
        self.solve(arr,idx+1)
        arr[idx]="1"
        self.solve(arr,idx+1)
    def binstr(self, n):
        # code here
        arr=["0"]*n
        self.result=[]
        self.solve(arr,0)
        
        return self.result 