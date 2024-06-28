class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # M, N = len(obstacleGrid), len(obstacleGrid[0])
        # hashmap = {}

        # def dfs(i, j):
        #     if i < 0 or j < 0 or i >= M or j >= N:
        #         return 0
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     if i == M-1 and j == N-1:
        #         return 1
        #     if (i, j) in hashmap:
        #         return hashmap[(i, j)]
            
        #     hashmap[(i, j)] = dfs(i+1, j) + dfs(i, j+1)
        #     return hashmap[(i, j)]
        
        # return dfs(0, 0)

        # M, N = len(obstacleGrid), len(obstacleGrid[0])
        # if obstacleGrid[M-1][N-1]:
        #     return 0

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * N
        dp[-1] = 1
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j == N-1:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j] + dp[j+1]
        return dp[0]