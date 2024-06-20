class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # M = len(grid)
        # N = len(grid[0])
        # visited = set()

        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= M or c >= N:
        #         return
        #     if grid[r][c] == "0":
        #         return
        #     if (r, c) in visited:
        #         return
            
        #     visited.add((r, c))

        #     dfs(r-1, c)
        #     dfs(r+1, c)
        #     dfs(r, c-1)
        #     dfs(r, c+1)

        # ans = 0
        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == "1" and (i, j) not in visited:
        #             dfs(i, j)
        #             ans += 1
        
        # return ans

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        M = len(grid)
        N = len(grid[0])
        visited = set()

        def bfs(i, j):
            q = deque([[i, j]])
            visited.add((i, j))

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if nr < 0 or nc < 0 or nr >= M or nc >= N:
                            continue
                        if (nr, nc) in visited or grid[nr][nc] == "0":
                            continue
                        q.append([nr, nc])
                        visited.add((nr, nc))

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    ans += 1
        return ans