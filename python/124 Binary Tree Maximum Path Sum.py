# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = root.val

        def solve(root):
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            left = max(left, 0)
            right = max(right, 0)

            self.maxVal = max(self.maxVal, root.val+left+right)
            return root.val + max(left, right)
        
        solve(root)
        return self.maxVal