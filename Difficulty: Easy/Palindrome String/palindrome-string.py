class Solution:
    def isPalindrome(self, s):
        # code here
        s2=s[::-1]
        
        if s!=s2:
            return False 
        else:
            return True 
