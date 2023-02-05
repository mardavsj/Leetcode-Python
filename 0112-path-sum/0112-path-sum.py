class Solution(object):
    def hasPathSum(self, root, targetSum):
        def helper(node,tot):
            if not node:
                return 
            elif not node.left and not node.right:
                if tot+node.val==targetSum:
                    return True
            else:
                return helper(node.left,tot+node.val) or helper(node.right,tot+node.val)
        if root:
            return helper(root,0)