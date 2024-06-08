# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

##### recap
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if len(preorder) == 0:
#             return
#         root = TreeNode(preorder[0])
#         rIdx = inorder.index(root.val)
#         root.left = self.buildTree(preorder[1: rIdx+1], inorder[:rIdx])
#         root.right = self.buildTree(preorder[rIdx+1:], inorder[rIdx+1:])

#         return root