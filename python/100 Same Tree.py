# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # def solve(p, q):
        #     if not p and not q:
        #         return True
        #     elif not p or not q:
        #         return False

        #     left = solve(p.left, q.left)
        #     right = solve(p.right, q.right)
        #     return left and right and p.val == q.val
        
        # return solve(p, q)

        def solve(p, q):
            if not p and not q:
                return True
            elif not p or not q or (p.val != q.val):
                return False

            return solve(p.left, q.left) and solve(p.right, q.right)
        
        return solve(p, q)