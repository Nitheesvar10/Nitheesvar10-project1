class Solution:
    def subCount(self, arr, k):
        cur_sum = 0
        count = 0
        
        hash = {0: 1}
        
        for num in arr:
            cur_sum += num
            
            rem = cur_sum % k
            
            if rem in hash:
                count += hash[rem]
            
            hash[rem] = hash.get(rem, 0) + 1
        
        return count