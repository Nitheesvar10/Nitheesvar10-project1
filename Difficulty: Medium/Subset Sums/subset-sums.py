class Solution:
    def solve(self,arr,idx,cur_sum):
        if idx==len(arr):
            self.result.append(cur_sum)
            return 
        
        self.solve(arr,idx+1,cur_sum+arr[idx])
        
        self.solve(arr,idx+1,cur_sum)
        
	def subsetSums(self, arr):
		# code here
		self.result=[]
		self.solve(arr,0,0)
		return self.result