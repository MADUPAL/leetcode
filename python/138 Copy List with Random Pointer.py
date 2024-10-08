"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copymap = {}
        
        dummy = Node(0)
        copy = dummy
        cur = head
        while cur:
            newNode = Node(cur.val)
            copy.next = newNode
            copymap[cur] = newNode
            cur = cur.next
            copy = copy.next
        

        cur = head
        copy = dummy.next
        while cur:
            if cur.random:
                copy.random = copymap[cur.random]
            else:
                copy.random = None
            copy = copy.next
            cur = cur.next
        
        return dummy.next