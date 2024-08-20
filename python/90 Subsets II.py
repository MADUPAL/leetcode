class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def subset(idx, s):
            if idx >= len(nums):
                ans.append(s.copy())
                return
            
            s.append(nums[idx])
            subset(idx+1, s)
            s.pop()

            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            subset(idx+1, s)
        
        subset(0, [])
        return ans