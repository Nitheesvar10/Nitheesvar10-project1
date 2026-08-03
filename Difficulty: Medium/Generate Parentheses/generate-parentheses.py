class Solution:
    
    def solve(self,idx,arr,n,open_b,close_b):
        if idx>=n:
            self.result.append("".join(arr))
            return 
        if open_b<self.max_pair:
            arr[idx]="("
            self.solve(idx+1,arr,n,open_b+1,close_b)
                
            
        if close_b<open_b:
            arr[idx]=")"
            self.solve(idx+1,arr,n,open_b,close_b+1)
            
    def generateParentheses(self, n):
        #code here
        self.result=[]
        arr=[""]*n
        self.max_pair=n//2
        self.solve(0,arr,n,0,0)
        return self.result 
