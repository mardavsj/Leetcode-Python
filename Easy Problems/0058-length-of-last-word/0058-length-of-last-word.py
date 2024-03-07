class Solution(object):
    def lengthOfLastWord(self, s):
        str_arr = s.split()
        
        if len(str_arr) == 0:
            return 0
        else:
            return len(str_arr[-1])
        