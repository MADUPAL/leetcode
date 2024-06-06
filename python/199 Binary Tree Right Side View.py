# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        q = deque()
        q.append(root)
        ans = []

        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if  node.left:
                    q.append(node.left)
                if  node.right:
                    q.append(node.right)
            ans.append(tmp[-1])
        
        return ans