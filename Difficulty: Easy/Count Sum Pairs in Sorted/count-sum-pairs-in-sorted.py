class Solution:
    def countPairs(self, arr, target): 
        left=0
        right=len(arr)-1
        count=0
        while left <right:
            sum=arr[left]+arr[right]
            
            if sum>target :
                right-=1
                
            elif sum<target:
                left+=1
                
            else:
                if arr[left]==arr[right]:
                    n=right-left+1
                    count+=n*(n-1)//2
                    break
                
                else:
                    left_count=1
                    right_count=1
                    
                    while left <right  and arr[left]==arr[left+1]:
                        left_count+=1
                        left+=1
                    while right >left and arr[right]==arr[right-1]:
                        right_count+=1
                        right-=1
                        
                    
                    count+=left_count*right_count 
                    left+=1
                    right-=1
                    
        return count
        #  Code Here
        