class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # M, N = len(grid), len(grid[0])
        # q = deque()
        # visited = set()
        # dr = [-1, 1, 0, 0]
        # dc = [0, 0, -1, 1]

        # total = 0
        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j] == 2:
        #             q.append([i, j])
        #             visited.add((i, j))
        #         elif grid[i][j] == 1:
        #             total += 1

        # t = -1
        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         for i in range(4):
        #             nr, nc = r + dr[i], c + dc[i]
        #             if nr < 0 or nc < 0 or nr >= M or nc >= N:
        #                 continue
        #             if (nr, nc) in visited or grid[nr][nc] != 1:
        #                 continue
                    
        #             grid[nr][nc] = 2
        #             total -= 1
        #             q.append([nr, nc])
        #             visited.add((nr, nc))
        #     t += 1

        # if total == 0:
        #     if t == -1:
        #         return 0
        #     else:
        #         return t
        # else:
        #     return -1

        M, N = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        total = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    total += 1

        t = 0
        while q and total > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if nr < 0 or nc < 0 or nr >= M or nc >= N:
                        continue
                    if (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    total -= 1
                    q.append([nr, nc])
                    visited.add((nr, nc))
            t += 1
        
        return t if total == 0 else -1