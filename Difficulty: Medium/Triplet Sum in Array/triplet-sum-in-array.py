class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        # result=[]
        arr.sort()
        n=len(arr)
        for i in range(n-2):
            if i >0 and  arr[i]==arr[i-1]:
                continue
            left=i+1
            right=n-1
            while (left<right):
                s=arr[i]+arr[left]+arr[right]
                
                if s==target:
                    return True 
                    
                elif s>target:
                    right-=1
                else:
                    left+=1
                    
            
                    
        return False 
                