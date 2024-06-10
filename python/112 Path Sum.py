# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        # if not root:
        #     return False
        
        # t -= root.val

        # if not root.left and not root.right and t == 0:
        #     return True
        # if self.hasPathSum(root.left, t):
        #     return True
        # if self.hasPathSum(root.right, t):
        #     return True
        
        # return False

        def dfs(node, s):
            if not node:
                return False
            s += node.val

            if not node.left and not node.right:
                return s == t
            
            return (dfs(node.left, s) or dfs(node.right, s))
        
        return dfs(root, 0)