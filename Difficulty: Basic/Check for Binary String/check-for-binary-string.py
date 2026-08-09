class Solution:
    def isBinary(self, s):
        # code here
        for i  in s :
            if i  not in ["1","0"]:
                return False 
        return True 