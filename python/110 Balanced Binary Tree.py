# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def solve(root):
            if not root:
                return 0
            
            l = solve(root.left)
            r = solve(root.right)
            if abs(l-r) > 1:
                self.flag = False
            return max(l, r) + 1
        
        solve(root)
        return self.flag