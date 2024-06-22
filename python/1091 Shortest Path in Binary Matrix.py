class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # if grid[0][0] == 1:
        #     return -1

        # N = len(grid)
        # dr = [-1, 1, 0, 0, -1, 1, 1, -1]
        # dc = [0, 0, -1, 1, 1, 1, -1, -1]
        # q = deque()
        # visited = set()

        # q.append([0, 0])
        # visited.add((0, 0))

        # length = 1
        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         if r == N-1 and c == N-1:
        #             return length
                
        #         for i in range(8):
        #             nr, nc = r + dr[i], c + dc[i]
        #             if nr < 0 or nc < 0 or nr >= N or nc >= N:
        #                 continue
        #             if (nr, nc) in visited or grid[nr][nc] == 1:
        #                 continue
        #             q.append([nr, nc])
        #             visited.add((nr, nc))
        #     length += 1
        # return -1

        N = len(grid)
        dr = [-1, 1, 0, 0, -1, 1, 1, -1]
        dc = [0, 0, -1, 1, 1, 1, -1, -1]
        q = deque()
        visited = set()

        q.append([0, 0, 1])
        visited.add((0, 0))

        while q:
            r, c, d = q.popleft()
            if r < 0 or c < 0 or r >= N or c >= N or grid[r][c] == 1:
                continue
            if r == N-1 and c == N-1:
                return d
            for i in range(8):
                nr, nc = r+dr[i], c+dc[i]
                if (nr, nc) not in visited:
                    q.append([nr, nc, d+1])
                    visited.add((nr, nc))
        return -1