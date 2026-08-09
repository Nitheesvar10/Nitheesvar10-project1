class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack=[]
        result=[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            
            while stack  and stack[-1]<=arr[i]:
                stack.pop()
                
            if stack and stack[-1]>arr[i]:
                result[i]=stack[-1]
                
                
            stack.append(arr[i])
        return result