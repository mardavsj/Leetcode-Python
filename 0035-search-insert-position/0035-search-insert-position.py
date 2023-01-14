import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)
        