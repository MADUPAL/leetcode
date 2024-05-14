class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start, vIdx = -1, -1
        # for i in range(len(nums)):
        #     if val == nums[i]:
        #         vIdx = i
        #         start = i
        #         break
        # if vIdx == -1: return len(nums)
        # for i in range(start, len(nums)):
        #     if nums[vIdx] == val and nums[i] != val:
        #         nums[vIdx], nums[i] = nums[i], nums[vIdx]
        #         vIdx += 1
        
        # return vIdx

        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        
        return idx