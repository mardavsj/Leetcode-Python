class Solution(object):
    def inorderTraversal(self, root):
        def dfs(root, ans):
            if not root:
                return None
            dfs(root.left, ans)
            ans += [root.val]
            dfs(root.right, ans)
        ans = []
        dfs(root, ans)
        return ans
        