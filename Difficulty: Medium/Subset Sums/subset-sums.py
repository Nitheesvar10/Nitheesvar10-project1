class Solution:
    def solve(self,idx,arr,total):
        if idx >=len(arr):
            self.result.append(total)
            return 
        
        self.solve(idx+1,arr,total+arr[idx])
        self.solve(idx+1,arr,total)
        
        
        
	def subsetSums(self, arr):
		# code here
		self.result=[]
		total=0
		self.solve(0,arr,total)
		return self.result 