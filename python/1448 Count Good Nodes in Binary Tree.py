# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, check):
            if not root:
                return 0
            
            ans = 1
            for n in check:
                if root.val < n:
                    ans = 0
            check.append(root.val)
            ans += solve(root.left, check)
            ans += solve(root.right, check)
            check.pop()

            return ans
        
        return solve(root, [])