import math 
class Solution:
    def deleteMid(self, s):
        # code here\
        size=len(s)
        mid=math.floor((size-1)/2)
        s.pop(mid)
        return s 
        