class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # hs = {}

        # def dfs(i, j):
        #     if i < 0 or j < 0 or i >= m or j >= n:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if (i, j) in hs:
        #         return hs[(i, j)]
            
        #     hs[(i, j)] = dfs(i+1, j) + dfs(i, j+1)

        #     return hs[(i, j)]
        
        # return dfs(0, 0)

        # dp = [[0] * n for _ in range(m+1)]
        # for i in range(m-1, -1, -1):
        #     dp[i][-1] = 1
        #     for j in range(n-2, -1, -1):
        #         dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        # return dp[0][0]

        dp = [0] * n
        for i in range(m-1, -1, -1):
            nxt = [0] * n
            nxt[-1] = 1
            for j in range(n-2, -1, -1):
                nxt[j] = dp[j] + nxt[j + 1]
            dp = nxt

        return dp[0]