class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            if target - n not in hashmap:
                hashmap[n] = i
            else:
                return [hashmap[target - n], i]
        
        # hm = {}

        # for i in range(len(nums)):
        #     if nums[i] not in hm:
        #         hm[target-nums[i]] = i
        #     elif nums[i] in hm:
        #         return [i, hm[nums[i]]]