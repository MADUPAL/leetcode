class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # M = len(grid)
        # N = len(grid[0])
        # dr = [-1, 1, 0, 0]
        # dc = [0, 0, -1, 1]
        # q = deque()
        # visited = set()

        # def bfs(i, j):
        #     q.append([i, j])
        #     visited.add((i, j))

        #     cnt = 0
        #     while q:
        #         for _ in range(len(q)):
        #             r, c = q.popleft()
        #             cnt += 1
        #             for i in range(4):
        #                 nr, nc = r+dr[i], c+dc[i]
        #                 if nr < 0 or nc < 0 or nr >= M or nc >= N:
        #                     continue
        #                 if (nr, nc) in visited or grid[nr][nc] == 0:
        #                     continue
        #                 q.append([nr, nc])
        #                 visited.add((nr, nc))

        #     return cnt

        # ans = 0
        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == 1 and (i, j) not in visited:
        #             ans = max(ans, bfs(i, j))
        
        # return ans

        M = len(grid)
        N = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= M or c >= N:
                return 0
            if (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            cnt = 1
            cnt += dfs(r-1, c)
            cnt += dfs(r+1, c)
            cnt += dfs(r, c-1)
            cnt += dfs(r, c+1)

            return cnt

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans = max(ans, dfs(i, j))
        
        return ans

            # cnt = 1
            # cnt += dfs(r-1, c)
            # cnt += dfs(r+1, c)
            # cnt += dfs(r, c-1)
            # cnt += dfs(r, c+1)

            # return cnt
            ### ===>>>
            # return (1 + dfs(r-1, c) +
            #             dfs(r+1, c) +
            #             dfs(r, c-1) +
            #             dfs(r, c+1)
            #         )