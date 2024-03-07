class Solution(object):
    def titleToNumber(self, columnTitle):
        corresponding_number = 0
        for i in range(len(columnTitle)):
            current_letter=columnTitle[i]
            corresponding_letter_value=ord(current_letter) - ord('A') + 1
            corresponding_number += (corresponding_letter_value *pow(26,len(columnTitle)-i-1))

        return corresponding_number    