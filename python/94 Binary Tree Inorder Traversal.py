# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []

        # def inorder(root):
        #     if not root:
        #         return None

        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)
        
        # inorder(root)

        # return ans

        ans = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        
        return ans