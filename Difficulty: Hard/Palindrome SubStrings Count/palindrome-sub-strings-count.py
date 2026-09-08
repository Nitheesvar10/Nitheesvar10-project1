class Solution:
    def countPS(self, s):
        # code here
        count=0
        for i in range(0,len(s)):
            count+=self.pal(s,i,i)
            count+=self.pal(s,i,i+1)
            
        return count 
        
    def pal(self,s,left,right):
        c=0
        while (left >=0 and right <len(s)) and  (s[left]==s[right]):
            if (right-left+1) >=2:
                c+=1
                
            left-=1
            right+=1
            
        return c 
            