class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums= set(nums)
        if len(set_nums) < len(nums):
            return True
        return False