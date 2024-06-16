class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            if target - n not in hashmap:
                hashmap[n] = i
            else:
                return [hashmap[target - n], i]