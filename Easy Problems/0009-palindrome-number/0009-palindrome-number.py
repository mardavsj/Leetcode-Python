class Solution(object):
    def isPalindrome(self, x):
        val = str(x)
        return val == val[::-1]
    
ob1 = Solution()
print(ob1.isPalindrome(424))
print(ob1.isPalindrome(-565))
        