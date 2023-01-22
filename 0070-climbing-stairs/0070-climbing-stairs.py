class Solution(object):
    def climbStairs(self, n):
        if n < 3: return n
        n_minus_2_combos = 1
        n_minus_1_combos = 2
        for step in range(n-2):
            curr_combos = n_minus_1_combos + n_minus_2_combos
            n_minus_2_combos = n_minus_1_combos
            n_minus_1_combos = curr_combos
        return curr_combos
        