class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
        return True 