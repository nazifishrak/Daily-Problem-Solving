# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = [root]
        out = []

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            inner = []
            
            for i in range(level_size):
                curr = queue.pop(0)
                
                if curr:
                    inner.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if inner:
                out.append(inner)
        
        return out
