# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### DFS
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left), dfs(root.right)) + 1
        
        # return dfs(root)

        ### BFS
        # if not root:
        #     return 0
        # q = deque()
        # q.append(root)
        # ans = 0

        # while q:
        #     ans += 1
        #     for _ in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        # return ans

        ### Iterative DFS
        stack = [[root, 1]]
        ans = 0

        while stack:
            node, depth = stack.pop()

            if node:
                ans = max(ans, depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
        
        return ans