class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()
        def dfs(r, c, idx):
            if idx >= len(word):
                return True
            if r >= R or c >= C or r < 0 or c < 0:
                return False
            if word[idx] != board[r][c]:
                return False
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            
            result = dfs(r-1, c, idx+1) or dfs(r+1, c, idx+1) or dfs(r, c-1, idx+1) or dfs(r, c+1, idx+1)

            visited.remove((r, c))

            return result
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:

                    if dfs(i, j, 0):
                        return True
        
        return False