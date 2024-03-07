class Solution(object):
    def mySqrt(self, x):
        if x == 1:
            return 1
        right = x//2
        left = 0
        while left <= right:
            mid = (left + right)//2
            temp_product = mid*mid
            if temp_product == x:
                return mid
            elif temp_product > x:
                right = mid - 1
            elif temp_product < x:
                left = mid + 1
        return right 