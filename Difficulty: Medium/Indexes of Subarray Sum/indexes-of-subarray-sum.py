class Solution:
    def subarraySum(self, arr, target):
        # code here
        hash={0:-1}
        cur_sum=0
        for i in range(len(arr)):
            cur_sum+=arr[i]
            
            e=cur_sum-target

            if e in hash:
                return [hash[e]+2,i+1]
            
            if cur_sum not in hash:
                hash[cur_sum]=i
            
        return [-1]
                
        