# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder(root):
            if not root:
                return None
            
            n1 = postorder(root.left)
            n2 = postorder(root.right)
            root.left, root.right = n2, n1
            return root
        
        return postorder(root)