import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        if((m+n)%2 != 0):
            mid = (m+n)//2 + 1
            return self.kthSmallest(nums1, nums2, 0, m-1, 0, n-1, mid)
        else:
            mid1 = int((m+n)/2)
            mid2 = int((m+n)/2) + 1
            return  (self.kthSmallest(nums1, nums2, 0, m-1, 0, n-1,mid1)+self.kthSmallest(nums1, nums2, 0, m-1, 0, n-1,mid2))/2
        
    def kthSmallest(self, num1, num2, start1, end1, start2, end2, k):
        # one list is empty, return the median in the other list
        
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if(start1 > end1):
            return num2[k-1]
        if(start2 > end2):
            return num1[k-1]
        if(k==1):
            if(num1[start1] < num2[start2]): 
                return num1[start1]
            else:
                return num2[start2]
        
        half1 = int(k*(len1/(len1+len2)))
        if(half1==0):
            half1 = 1
        
        half2 = k - half1
        
        print([start1,start2,half1,half2])
        mid1 = start1 + half1 - 1
        mid2 = start2 + half2 - 1
        print([mid1,mid2,k])
        print(start1,end1,start2,end2)
        if(num1[mid1] < num2[mid2]):
            k = k - half1
            start1 = mid1+1
            end2 = mid2
        else:
            k = k - half2
            start2 = mid2+1
            end1 = mid1
        print(start1,end1,start2,end2,k)
        return self.kthSmallest(num1, num2, start1, end1, start2, end2, k)