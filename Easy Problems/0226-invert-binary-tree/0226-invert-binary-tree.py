class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        leftSide = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(leftSide)
        return root