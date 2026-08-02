class Solution:
    def scoreOfParentheses(self, s):
        # code here 
        stack=[0]
        for  i in range(len(s)):
            if s[i]=="(":
                stack.append(0)
            else:
                if stack:
                    a=max(stack.pop()*2,1)
                    b=stack.pop()
                    a=a+b
                    stack.append(a)
        return stack[-1]
        
        