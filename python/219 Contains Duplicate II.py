class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = set()
        L = 0

        for R in range(len(nums)):
            if R-L > k:
                hs.remove(nums[L])
                L += 1
            if nums[R] in hs:
                return True
            hs.add(nums[R])
        
        return False