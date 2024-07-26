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
    
        # ans = []

        # def subset(idx, s):
        #     if idx >= len(nums):
        #         ans.append(s.copy())
        #         return
            
        #     s.append(nums[idx])
        #     subset(idx+1, s)
        #     s.pop()
        #     subset(idx+1, s)
        
        # subset(0, [])
        # return ans