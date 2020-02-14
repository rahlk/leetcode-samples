from collections import defaultdict
import bisect
class Solution(object):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def threeSum(self, nums):
            ans = []
            counter = defaultdict(int)
            for num in nums:
                counter[num] += 1
            nums = sorted(counter)
            
            for i, a in enumerate(nums):  
                two_sum = 0 - a
                left = bisect.bisect_left(nums, two_sum - nums[-1], i + 1)   
                right = bisect.bisect_right(nums, two_sum // 2, left)        
                for b in nums[left:right]:
                    c = two_sum - b
                    if c in counter and c > b:
                        ans.append([a, b, c])     # three different elements
                if counter[a] >= 2:
                    c = 0 - 2*a
                    if c in counter and c != a:
                        ans.append([a, a, c])     # two different elements
                    if counter[a] >= 3:
                        if a*3 == 0:
                            ans.append([a, a, a]) # one different elements
            return ans