class Solution:
    def minParentheses(self, s):
        # code here
        stack=[]
        closing=0
        for i in range(len(s)):
            if s[i] in ("(","[","{"):
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                else:
                    closing+=1
        return closing+len(stack)
            
        