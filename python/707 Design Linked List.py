class ListNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, nxt, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, nxt, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, nxt, prev = ListNode(val), cur, cur.prev
            prev.next = node
            nxt.prev = node
            node.prev = prev
            node.next = nxt

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            nxt, prev = cur.next, cur.prev
            prev.next = nxt
            nxt.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)