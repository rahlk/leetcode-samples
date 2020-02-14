class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        l = len(nums)
        if (l<3):
            return result
        for i in range(0,l):
            j = i+1
            k = l-1
            while(j<k):
                if(nums[i]+nums[j]+nums[k] == 0):
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    result.add(tuple(temp))
                    j = j+1
                    k = k-1
                elif nums[i]+nums[j]+nums[k] < 0 :
                    j = j+1
                else:
                    k = k-1
        return result