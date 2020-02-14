class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the numbers: timsort - O(nlgn)
        nums.sort()
        numel = len(nums)
        solutions = set()
        unique_nums = set(nums)
        # Edge cases: (a) empty; (b) all zeros
        if len(unique_nums) == 0:
            return []
        if len(unique_nums) == 1 and 0 in unique_nums and len(nums) == 3:
            return [3*[0]]
        
        for i in range(numel-2):
            start = i + 1
            end = numel - 1
            while start < end:
                three_sum = nums[i] + nums[start] + nums[end]
                if three_sum == 0:
                    solutions.add((nums[start], nums[i], nums[end]))
                    start += 1
                    end -= 1
                elif three_sum < 0:
                    start += 1
                elif three_sum > 0:
                    end -= 1
        
        return list(map(list, solutions))
            