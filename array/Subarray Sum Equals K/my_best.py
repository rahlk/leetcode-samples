class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {0: 1}
        sum_ = 0
        count = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            
            remains = sum_ - k
            
            if remains in hashmap:
                count += hashmap[remains]
                
            if sum_ not in hashmap:
                hashmap[sum_] = 1
            else:
                hashmap[sum_] += 1
            
        
        return count