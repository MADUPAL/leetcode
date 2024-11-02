class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(idx, c, s):
            if idx >= len(candidates) or s > target:
                return
            if s == target:
                ans.append(c.copy())
                return

            for i in range(idx, len(candidates)):
                c.append(candidates[i])
                solve(i, c, s + candidates[i])
                c.pop()
        
        solve(0, [], 0)

        return ans