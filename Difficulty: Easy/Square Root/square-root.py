class Solution:
    def floorSqrt(self, n): 
        # code here
        if n<=1:
            return 1
            
        left=1
        right=n//2
        
        while left<=right:
            mid=left+(right-left)//2
            
            sq=mid*mid
            
            if sq==n:
                return mid 
                
            elif sq>n:
                right=mid-1
                
            else:
                left=mid+1
                
            
        return right 
            