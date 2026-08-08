from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        result=[0]*(len(arr)-k+1)
        
        q=deque([])
        
        for right in range(len(arr)):
            
            while q and q[0] <=right-k:
                q.popleft()
                
            while q and arr[q[-1]] <arr[right]:
                q.pop()
                
            q.append(right)
            
            
            if right >=k-1:
                result[right-k+1]=arr[q[0]]
                
        return result 