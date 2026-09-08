
class Solution:
    def longestPalindrome(self, s):
        # code here
        start=0
        end=0
        for i in range(len(s)):
            odd_len=self.pal(s,i,i)
            even_len=self.pal(s,i,i+1)
            
            max_len=max(odd_len,even_len)
            
            if max_len>(end-start+1):
                start=i-(max_len-1)//2
                end=i+(max_len)//2
                
        return s[start:end+1]
        
    def pal(self,s,left,right):
        while left>=0 and right <len(s) and s[left]==s[right]:
            left-=1
            right+=1
            
        return right-left-1
        
    