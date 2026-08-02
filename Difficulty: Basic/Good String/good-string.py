class Solution:
    def isGoodString(self, s: str) -> bool:
        # code here.
        stack=[]
        for i in range(len(s)):
            if i ==0:
                stack.append(s[i])
                
            else:
                dif=abs(ord(s[i])-ord(stack[-1]))
                if min(dif,26-dif)!=1:
                    return False 
                stack.append(s[i])
        if len(stack)==len(s):
            return True 
                