# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.LCA = TreeNode(float("inf"))
        if p.val > q.val:
            p, q = q, p

        def search(root, target):
            if not root:
                return False
            if root.val < target:
                return search(root.right, target)
            elif root.val > target:
                return search(root.left, target)
            else:
                return True
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            t1 = search(root.left, p.val)
            t2 = search(root.right, q.val)
            if (root.val == p.val and t2) or (root.val == q.val and t1) or (t1 and t2):
                self.LCA = root if self.LCA.val > root.val else self.LCA
            inorder(root.right)
        
        inorder(root)
        return self.LCA