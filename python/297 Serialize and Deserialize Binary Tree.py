# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        def preorder(root):
            if not root:
                s.append("N")
                return
            s.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ",".join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(",")
        self.idx = 0

        def preorder():
            if s[self.idx] == "N":
                self.idx += 1
                return None
            
            newNode = TreeNode(int(s[self.idx]))
            self.idx += 1
            newNode.left = preorder()
            newNode.right = preorder()

            return newNode
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))