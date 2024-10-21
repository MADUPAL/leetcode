# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.maxVal = float("-inf")

        def solve(root):
            if not root:
                return True
            
            ans = True
            ans &= solve(root.left)
            if self.maxVal < root.val:
                self.maxVal = root.val
            else:
                ans = False
            
            ans &= solve(root.right)

            return ans
        
        return solve(root)