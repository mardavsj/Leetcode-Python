class Solution:
    def isHappy(self, n):
        seen = set()
        while True:
            if n==1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
                n = sum(int(i)**2 for i in str(n))