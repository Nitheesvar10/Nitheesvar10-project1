class Solution:
    def decodedString(self, s):
        # code here
        stack=[["",1]]
        num=""
        for i in s:
            if i.isdigit():
                num+=i
                
            elif i=="[":
                stack.append(["",int(num)])
                num=""
                
            elif i=="]":
                string_,k=stack.pop()
                stack[-1][0]+=string_*k
            else:
                stack[-1][0]+=i
                
        return stack[-1][0]
                
                
        