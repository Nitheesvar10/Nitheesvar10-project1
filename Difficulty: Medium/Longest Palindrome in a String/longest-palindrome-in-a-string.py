
class Solution:
    def longestPalindrome(self, s):
        # code here
        start=0
        end=0
        
        for i in range(len(s)):
            even_pal=self.pal(s,i,i+1)
            odd_pal=self.pal(s,i,i)
            
            max_lenght=max(even_pal,odd_pal)
            
            if max_lenght>(end-start+1):
                start=i-(max_lenght-1)//2
                end=i+(max_lenght)//2
                
        return s[start:end+1]
        
    def pal(self,s,left,right):
        while left>=0 and right <len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return  right-left-1