class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_type = 0
        nums2_type = 0
        nums1_m = 0
        nums2_m = 0
        nums1_l_pt = 0
        nums1_r_pt = 0
        nums2_l_pt = 0
        nums2_r_pt = 0
        
        if len(nums1) == 0 or len(nums2) == 0:
            x = nums1 + nums2
            if len(x)%2 == 1:
                return(x[int(len(x)/2)])
            else:
                return((x[int(len(x)/2)] + x[int(len(x)/2)-1]) / 2)
        
        # nums1 median
        if len(nums1)%2 == 1:
            nums1_m = nums1[int(len(nums1)/2)]
        else:
            nums1_m = (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1]) / 2
            nums1_type = 1
        # nums2 median
        if len(nums2)%2 == 1:
            nums2_m = nums2[int(len(nums2)/2)]
        else:
            nums2_m = (nums2[int(len(nums2)/2)] + nums2[int(len(nums2)/2)-1]) / 2
            nums2_type = 1
        
        # set left and right bounds
        if nums1_m > nums2_m:
            nums1_r_pt = int(len(nums1)/2)
            nums2_l_pt = int(len(nums2)/2) - nums2_type
            for i in range(len(nums1)):
                if nums1[i] < nums2[nums2_l_pt]:
                    nums1_l_pt = i
                else:
                    nums1_l_pt = i
                    break
            for i in range(len(nums2)-1, 0, -1):
                if nums2[i] > nums1[nums1_r_pt]:
                    nums2_r_pt = i
                else:
                    nums2_r_pt = i
                    break
        elif nums1_m < nums2_m:
            nums1_l_pt = int(len(nums1)/2) - nums1_type
            nums2_r_pt = int(len(nums2)/2)
            for i in range(len(nums2)):
                if nums2[i] < nums1[nums1_l_pt]:
                    nums2_l_pt = i
                else:
                    nums2_l_pt = i
                    break
            for i in range(len(nums1)-1, 0, -1):
                if nums1[i] > nums2[nums2_r_pt]:
                    nums1_r_pt = i
                else:
                    nums1_r_pt = i
                    break
        else:
            return(nums1_m)
        
        # get new array x
        x = nums1[nums1_l_pt:nums1_r_pt+1] + nums2[nums2_l_pt:nums2_r_pt+1]
        x.sort()
        
        # balance left and right numbers
        l_num = nums1_l_pt + nums2_l_pt
        r_num = (len(nums1) - nums1_r_pt - 1) + (len(nums2) - nums2_r_pt - 1)
        if l_num > r_num:
            x = x[:len(x)-(l_num-r_num)]
        elif l_num < r_num:
            x = x[(r_num-l_num):]
        
        # get x median
        if len(x)%2 == 1:
            return(x[int(len(x)/2)])
        else:
            return((x[int(len(x)/2)] + x[int(len(x)/2)-1]) / 2)