class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode("dummy")
        self.right = ListNode("dummy")

        self.cur = ListNode(homepage)
        self.left.next = self.cur
        self.right.prev = self.cur
        self.cur.next = self.right
        self.cur.prev = self.left

    def visit(self, url: str) -> None:
        node, nxt, prev = ListNode(url), self.right, self.cur
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

        self.cur = node

    def back(self, steps: int) -> str:
        cur = self.cur
        while cur and steps > 0:
            if cur == self.left:
                break
            cur = cur.prev
            steps -= 1
        
        if cur == self.left:
            self.cur = cur.next
        else:
            self.cur = cur

        return self.cur.val
        
    def forward(self, steps: int) -> str:
        cur = self.cur
        while cur and steps > 0:
            if cur == self.right:
                break
            cur = cur.next
            steps -= 1
        
        if cur == self.right:
            self.cur = cur.prev
        else:
            self.cur = cur

        return self.cur.val

# class ListNode:
#     def __init__(self, val: str, prev=None, next=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.cur = ListNode(homepage)

#     def visit(self, url: str) -> None:
#         self.cur.next = ListNode(url, self.cur)
#         self.cur = self.cur.next

#     def back(self, steps: int) -> str:
#         while self.cur.prev and steps > 0:
#             self.cur = self.cur.prev
#             steps -= 1

#         return self.cur.val

#     def forward(self, steps: int) -> str:
#         while self.cur.next and steps > 0:
#             self.cur = self.cur.next
#             steps -= 1

#         return self.cur.val