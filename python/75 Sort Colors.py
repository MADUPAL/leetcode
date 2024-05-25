class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket = [0] * 3

        # for n in nums:
        #     bucket[n] += 1
        
        # x = 0
        # for n in range(len(bucket)):
        #     for _ in range(bucket[n]):
        #         nums[x] = n
        #         x += 1

        L, R = 0, len(nums) - 1

        i = 0
        while i <= R:
            if nums[i] == 0:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
            elif nums[i] == 2:
                nums[i], nums[R] = nums[R], nums[i]
                R -= 1
                i -= 1
            i += 1