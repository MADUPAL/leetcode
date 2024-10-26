class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        trie = Trie()

        for word in words:
            trie.addWord(word)
        
        visited = set()
        ans = set()

        def dfs(r, c, node, word):
            if r >= R or c >= C or r < 0 or c < 0:
                return
            if (r, c) in visited:
                return
            if board[r][c] not in node.children:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                ans.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visited.remove((r, c))
        
        root = trie.root
        for i in range(R):
            for j in range(C):
                dfs(i, j, root, "")
        
        return list(ans)