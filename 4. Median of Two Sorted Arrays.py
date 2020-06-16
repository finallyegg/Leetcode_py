# hard
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # intuition: find a partition line cut through both
        # [1,2,4 / 12 , 15 ]
        # [3,5,8 / 45, 68, 120 ,155]
        # make sure every element in the left is less than every element in the right
        # And left item more thank right
        # set an init cutting line like in single array
        # [0,1,2] (0+2+1)/2
        # [0,1] (0+1+1)/2
        # [0,1,\2,3,4]
        # [5,6,7,8\,9,10]

        total_len = len(nums1) + len(nums2)

        l = 0
        r = len(nums1)

        while True:
            l1 = None
            l2 = None
            r1 = None
            r2 = None
            left = []
            right = []
            nums1cut = (l + r + 1)//2
            nums2cut = (total_len+1)//2 - nums1cut
            if nums1cut >= 0:
                if nums1[:nums1cut]:
                    l1 = nums1[nums1cut-1]
                    left.append(l1)
                if nums1cut < len(nums1):
                    r1 = nums1[nums1cut]
                    right.append(r1)
            if nums2cut >= 0:
                if nums2[:nums2cut]:
                    l2 = nums2[nums2cut-1]
                    left.append(l2)
                if nums2cut < len(nums2):
                    r2 = nums2[nums2cut]
                    right.append(r2)

            o1 = l1 == None or r2 == None or (l1 <= r2)
            o2 = l2 == None or r1 == None or (l2 <= r1)

            if o1 and o2:
                if total_len % 2:
                    return max(left)
                else:
                    return (max(left) + min(right))/2

            if not o1:
                r -= 1
            else:
                l += 1
