class Solution:
    def countPairs(self, arr, target): 
        #  Code Here\
        left=0
        count=0
        right=len(arr)-1
        while left<right:
            summ=arr[left]+arr[right]
            
            if summ>target:
                right-=1
            elif summ<target:
                left+=1
            else:
                if arr[left]==arr[right]:
                    n=right-left+1
                    count+=n*(n-1)//2
                    break
                
                left_count=1
                while left+1<right  and arr[left+1]==arr[left]:
                    left_count+=1
                    left+=1
                    
                right_count=1
                while right-1>left and arr[right-1]==arr[right]:
                    right_count+=1
                    right-=1
                
                count+=right_count*left_count 
                right-=1
                left+=1
        return count

            