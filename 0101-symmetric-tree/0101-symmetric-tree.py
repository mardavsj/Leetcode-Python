class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [(root, root)]
        
        while stack: 
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                pass
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:    
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            
        return True