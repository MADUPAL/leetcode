class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # L = 1
        # k = 1
        # for R in range(1, len(nums)):
        #     if nums[R-1] == nums[R] and k < 2:
        #         k += 1
        #         nums[L] = nums[R]
        #         L += 1
        #     elif nums[R-1] != nums[R]:
        #         k = 1
        #         nums[L] = nums[R]
        #         L += 1
        
        # return L

        L, R = 0, 0
        while R < len(nums):
            idx, temp = R, nums[R]

            while R < len(nums) and nums[R] == temp:
                R += 1
            
            k = 2 if R-idx > 2 else R-idx
            # k = min(2, R-idx)

            while k > 0:
                k -= 1
                nums[L] = temp
                L += 1
        
        return L