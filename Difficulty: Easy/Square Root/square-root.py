class Solution:
    def floorSqrt(self, n): 
        # code here
        if n<=1:
            return n
            
        left=1
        right=n//2
        
        while left<=right:
            mid=left+(right-left)//2
            
            if mid*mid==n:
                return mid
                
            if (mid*mid)<n:
                left=mid+1
                
            else:
                right=mid-1
                
        return right 
                
        
                
            