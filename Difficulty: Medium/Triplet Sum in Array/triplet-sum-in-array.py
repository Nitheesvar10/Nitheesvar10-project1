class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        result=[]
        
        for i in range(0,len(arr)-2):
            if i >0 and  arr[i]==arr[i-1]:
                continue 
            left=i+1
            right=len(arr)-1
            
            while left<right:
                sum=arr[left]+arr[right]+arr[i]
                
                if sum >target :
                    right-=1
                    
                elif sum <target:
                    left+=1
                    
                else:
                    result.append([i,left,right])
                    
                    while left<right  and arr[left]==arr[left+1]:
                        left+=1
                    while right >left  and arr[right]==arr[right-1]:
                        right-=1
                        
                    
                    left+=1
                    right-=1
                    
        if result :
            return True 
            
        else:
            return False 