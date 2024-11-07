class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(idx, cur, s):
            if s == target:
                ans.append(cur.copy())
                return
            
            if idx >= len(candidates) or s > target:
                return
            
            cur.append(candidates[idx])
            solve(idx, cur, s + candidates[idx])
            cur.pop()
            solve(idx+1, cur, s)
        
        solve(0, [], 0)

        return ans