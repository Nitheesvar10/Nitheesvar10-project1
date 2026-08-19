class Solution:
    def findEquilibrium(self, arr):
        # code here
        
        pref=[0]*len(arr)
        suf=[0]*len(arr)
        pref[0]=arr[0]
        suf[len(arr)-1]=arr[len(arr)-1]


        for i in range(1,len(arr)):
            pref[i]=arr[i]+pref[i-1]
            
        for i in range(len(arr)-2,-1,-1):
            suf[i]=arr[i]+suf[i+1]
            
        for i in range(0,len(arr)):
            if pref[i]==suf[i]:
                return i
        
        return -1 
