class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        maps = [["."]*n for _ in range(n)]
        colSet = set()
        posDSet = set()
        negDSet = set()

        ans = []

        def solve(row):
            if row >= n:
                copy = [''.join(r) for r in maps]
                ans.append(copy)
                return
            
            for col in range(n):
                if col in colSet or ((row+col) in posDSet) or ((row-col) in negDSet):
                    continue
                
                maps[row][col] = "Q"
                colSet.add(col)
                posDSet.add(row+col)
                negDSet.add(row-col)
                solve(row+1)
                maps[row][col] = "."
                colSet.remove(col)
                posDSet.remove(row+col)
                negDSet.remove(row-col)
        
        solve(0)

        return ans