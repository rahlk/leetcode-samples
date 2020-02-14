class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return
        
        if not nums1:
            l = len(nums2)
            if l%2: # <--- odd
                return nums2[int(l/2)]
            else:
                return (nums2[int(l/2)-1] + nums2[int(l/2)]) / 2
        
        if not nums2:
            l = len(nums1)
            if l%2: # <--- odd
                return nums1[int(l/2)]
            else:
                return (nums1[int(l/2)-1] + nums1[int(l/2)]) / 2
        
        # Make x the smaller of the two arrays and y the larger
        if len(nums2) < len(nums1):
            x = nums2
            y = nums1
        else:
            x = nums1
            y = nums2
        
        # Compute the lengths of x and y
        m = len(x)
        n = len(y)
        
        # Binary search on the smallest array (x)
        lo = 0
        hi = m 
        
        part_xy = int((m+n+1) / 2) # ----> if m+n is odd, the left partition will be 1 more than the right
        
        while lo <= hi:
            part_x = int((lo + hi)/2)
            part_y = part_xy - part_x
            
            # print(part_x, part_y)
            # Boundaries
            left_x = -1e32 if part_x == 0 else x[part_x-1]
            left_y = -1e32 if part_y == 0 else y[part_y-1]
            
            right_x = 1e32 if part_x == m else x[part_x]
            right_y = 1e32 if part_y == n else y[part_y]
            
            if left_x <= right_y and left_y <= right_x:
                # We can comptue the median
                if ((m+n) % 2) == 0: # <----- even
                    return (max(left_x, left_y) + min(right_x, right_y)) / 2
                else:
                    return max(left_x, left_y)
            
            else:
                if left_x > right_y:
                    hi = part_x - 1
                
                elif left_y > right_x:
                    lo = part_x + 1
        