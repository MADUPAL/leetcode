class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checkRCSet = set()
        # checkSqSet = set()

        # def check(x, y):
        #     if (x, y) in checkRCSet and (3*(x//3), 3*(y//3)) in checkSqSet:
        #         return True
        #     row, col, square = set(), set(), set()
            
        #     for i in range(9):
        #         if board[x][i] == '.':
        #             continue
        #         if board[x][i] in row:
        #             return False
        #         else:
        #             row.add(board[x][i])

        #     for i in range(9):
        #         if board[i][y] == '.':
        #             continue
        #         if board[i][y] in col:
        #             return False
        #         else:
        #             col.add(board[i][y])
        #     checkRCSet.add((x, y))

        #     sx, sy = 3*(x//3), 3*(y//3)
        #     for i in range(sx, sx+3):
        #         for j in range(sy, sy+3):
        #             if board[i][j] == '.':
        #                 continue
        #             if board[i][j] in square:
        #                 return False
        #             else:
        #                 square.add(board[i][j])
        #     checkSqSet.add((sx, sy))

        #     return True

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             if not check(i, j):
        #                 return False
        
        # return True

        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i//3, j//3)]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i//3, j//3)].add(board[i][j])
        
        return True