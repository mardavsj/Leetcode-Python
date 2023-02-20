class Solution(object):
    def postorderTraversal(self, root):
        def traverse(node):
		if node is None: return []
		l = traverse(node.left)
		r = traverse(node.right)
		return l + r + [node.val] 
	return traverse(root)