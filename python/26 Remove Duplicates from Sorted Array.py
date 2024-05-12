
class Solution:
    def removeDuplicates(self, nums) -> int:

        # k = 1
        # dIdx = 1
        # cur = nums[0]

        # for i in range(1, len(nums)):
        #     if cur != nums[i]:
        #         nums[dIdx] = nums[i]
        #         cur = nums[i]
        #         k += 1
        #         dIdx += 1

        # return k

        uIdx = 1

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[uIdx] = nums[i]
                uIdx += 1
        
        return uIdx