class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # M = len(matrix[0])
        # N = len(matrix)

        # l, r = 0, M*N-1

        # while l <= r:
        #     m = (l+r)//2
        #     x = m // M
        #     y = m % M
        #     # x, y = divmod(m, M)
        #     if matrix[x][y] < target:
        #         l = m + 1
        #     elif matrix[x][y] > target:
        #         r = m - 1
        #     else:
        #         return True
        
        # return False

        M = len(matrix[0])
        N = len(matrix)

        top, bot = 0, N-1

        while top <= bot:
            row = (top+bot)//2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top+bot)//2
        l, r = 0, M-1

        while l <= r:
            m = (l+r)//2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False