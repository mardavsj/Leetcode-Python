class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) - 1 and not s[i].isalnum():
                i += 1
                
            while j >= 1 and not s[j].isalnum():
                j -= 1
                
            if not s[i].isalnum() or not s[j].isalnum():
                return True
                
            if s[i].lower() != s[j].lower():
                print("{} ({}), {} ({})".format(s[i], i, s[j], j))
                return False
        
            i += 1
            j -= 1
        
        return True
        