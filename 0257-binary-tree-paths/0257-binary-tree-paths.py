class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def solve(root, s):
            s += str(root.val)
            if not root.right and not root.left:
                ans.append(s)
                return
            if root.right:
                solve(root.right, s+"->")
            if root.left:
                solve(root.left, s+"->")
        solve(root, "")
        return ans