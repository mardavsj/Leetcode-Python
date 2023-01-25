class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last1 = m - 1
        last2 = n - 1
        last = m + n - 1

        while last1 >= 0 and last2 >= 0:
            if nums1[last1] > nums2[last2]:
                nums1[last] = nums1[last1]
                last1 -= 1
                last -= 1
            else:
                nums1[last] = nums2[last2]
                last2 -= 1
                last -= 1

        while last2 >= 0:
            nums1[last] = nums2[last2]
            last -= 1
            last2 -= 1
        