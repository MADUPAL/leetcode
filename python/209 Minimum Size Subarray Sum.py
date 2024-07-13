class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, L = 0, 0
        ans = 100001

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                ans = min(ans, R-L+1)
                total -= nums[L]
                L += 1
        
        return 0 if ans == 100001 else ans