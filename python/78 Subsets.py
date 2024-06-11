class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        cur = []
        def dfs(idx):
            if idx >= len(nums):
                ans.append(cur.copy())
                return
            
            cur.append(nums[idx])
            dfs(idx+1)

            cur.pop()
            dfs(idx+1)

        dfs(0)

        return ans