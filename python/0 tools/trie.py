# purpose of Trie

# Insert Word O(1)
# Search Word O(1)
# Prefix Search O(1)

class TrieNode:
    def __init__(self):
        self.parent = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.parent:
                cur.parent[c] = TrieNode()
            cur = cur.parent[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.parent:
                return False
            cur = cur.parent[c]
        
        return cur.word

    def prefixSearch(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.parent:
                return False
            cur = cur.parent[c]
        
        return True