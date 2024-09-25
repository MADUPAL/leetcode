class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums)-1

        # while l <= r:
        #     print(l, r)
        #     m = (l+r)//2
        #     if nums[m] == target:
        #         return m
            
        #     if nums[l] <= nums[r]:
        #         if target > nums[m]:
        #             l = m+1
        #         else:
        #             r = m-1
        #     elif target < nums[l]:
        #         l += 1
        #     elif target >= nums[l]:
        #         r -= 1

        # return -1

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1

        return -1