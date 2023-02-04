class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d))
        