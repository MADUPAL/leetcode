class Solution:

    def rob(self, nums: List[int]) -> int:
        # s = {}
        # s[0] = nums[0]

        # def f(n):
        #     if n < 0:
        #         return 0
        #     if n in s:
        #         return s[n]
            
        #     s[n] = max(nums[n] + f(n-2), f(n-1))
        #     return s[n]
        
        # return f(len(nums)-1)

        r1, r2 = 0, 0
        for n in nums:
            r1, r2 = r2, max(n + r1, r2)
        return r2