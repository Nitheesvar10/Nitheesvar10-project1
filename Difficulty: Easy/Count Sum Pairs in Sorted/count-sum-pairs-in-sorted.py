class Solution:
    def countPairs(self, arr, target): 
        #  Code Here
    
        arr.sort()
        left=0
        
        count=0
        right=len(arr)-1
        while left<right :
            summ=arr[left]+arr[right]
            if summ>target:
                right-=1
            elif summ<target:
                left+=1
                
            else:
                if  arr[left]==arr[right]:
                    n=right-left+1
                    count+=n*(n-1)//2
                    break
                
                left_count=1
                while left<right and arr[left] ==arr[left+1]:
                    left_count+=1
                    left+=1
                    
                right_count=1
                while right>left  and arr[right]==arr[right-1]:
                    right_count+=1
                    right-=1
                
                count+=left_count *right_count 
                left+=1
                right-=1
                
        return count 
                    
                    
