class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        if len(nums) == 0:
            return 0
        c = [0] * (len(nums) + 1)
        d = {}
        d["0"] = 1
        for i, n in enumerate(nums):
            c[i+1] = c[i] + n
            if str(c[i+1] - k) in d.keys():
                counter += d[str(c[i+1] - k)]
            if str(c[i+1]) not in d.keys():
                d[str(c[i+1])] = 0
            d[str(c[i+1])]+=1
            
            
        return counter