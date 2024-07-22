class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(root, idx):
            cur = root
            for i in range(idx, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            
            return cur.word
        
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)