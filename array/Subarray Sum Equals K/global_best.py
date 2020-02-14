class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum, ways = 0, 0
        mem = {0: 1}
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum - k in mem:
                ways += mem[curr_sum - k]
            
            if curr_sum in mem:
                mem[curr_sum] += 1
            else:
                mem[curr_sum] = 1
                
        return ways
                